from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import io
import PyPDF2
import os,random
from django.db import connection
from django.http import FileResponse
from .utils import render_to_pdf
from django.template.loader import get_template
from rlextra.utils.pdfencrypt import encryptCanvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from update.views import smsender
from update.forms import captcha
import pyodbc
# Create your views here.
uidai_con = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.33.62,1433;DATABASE=uidai;UID=uidai;PWD=uidai")
uidai_cur = uidai_con.cursor()
#cursor = connection.cursor()


def download(request):
    if request.method == 'POST':
        aadhar_num = request.POST['aadhar_num']
        uidai_cur.execute('SELECT phone FROM details WHERE aadhar_num={}'.format(aadhar_num))
        phone_num=uidai_cur.fetchone()
        #a = Sms('9121587454','Shiva@01')
        smss = smsender()
        otp=random.randint(100000,999999)
        phone_num=phone_num[0]
        print(phone_num)
        print(type(phone_num))
        #a.send(phone_num,str(otp))
        print(otp)
        smss.send_sms(otp, phone_num)
        uidai_cur.execute("INSERT INTO verify_otp VALUES ({},{},{})".format(aadhar_num,phone_num,otp))
        uidai_cur.commit()
        return render(request,"aadharcard/enter_otp.html",{'phone_num': phone_num})
    return render(request,'aadharcard/card_number.html')

def aadhar_card(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        phone_num = request.POST['phone_num']
        uidai_cur.execute("SELECT otp,aadhar_num FROM verify_otp WHERE phone_num={}".format(phone_num))
        real_otp = uidai_cur.fetchone()
        aadhar_num = real_otp[1]
        print(real_otp[0])
        print(otp)
        if int(otp) == int(real_otp[0]):
            uidai_cur.execute("DELETE FROM verify_otp WHERE phone_num={}".format(phone_num))
            uidai_cur.commit()
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = "filename=narendra.pdf"
            p = canvas.Canvas(response)
            #encryptCanvas(p, "narendra")
            x=30
            y=9.5*72
            p.rect(30,3*72,255,8.5*72,stroke=1,fill=0)
            p.rect(300,3*72,254,8.5*72,stroke=1,fill=0)
            p.drawInlineImage('top.PNG',x,y,width=254,height=140)
            p.drawInlineImage('back.PNG',300,7.4*72,width=253,height=290)
            uidai_cur.execute('SELECT * FROM details WHERE aadhar_num={};'.format(aadhar_num))
            parse = uidai_cur.fetchone()
            print(parse)
            p.setFont('Helvetica', 11)
            x=x+40
            y=y-22
            line3="Enrolment.no.:2017/78007/93872"
            p.drawString(x,y,line3)
            y=y-18
            line4=parse[3]+' '+parse[1]+' '+parse[2]
            p.drawString(x, y, line4)
            y=y-18
            line2='Gender:'+' '+parse[4]
            p.drawString(x, y, line2)
            y=y-18
            line5='S/O:'+' '+parse[5]
            p.drawString(x, y, line5)
            y=y-18
            line6='DO NO:'+' '+parse[11]
            p.drawString(x, y, line6)
            uidai_cur.execute('SELECT * FROM pincodes WHERE pincode={}'.format(parse[12]))
            det = uidai_cur.fetchone()
            y=y-18
            line8=det[1]
            p.drawString(x, y, line8)
            y=y-18
            line9=det[2]+' - '+str(det[0])
            p.drawString(x, y, line9)
            uidai_cur.execute('SELECT state FROM states WHERE id={}'.format(det[3]))
            state = uidai_cur.fetchone()
            y=y-18
            line10=state[0]
            p.drawString(x, y, line10)
            y=y-18
            line12=str(parse[9])
            p.drawString(x, y, line12)
            y=y-80
            line13="Your Aadhar number.:"
            p.drawString(x, y, line13)
            y=y-25
            num = str(parse[0])
            line14=str(num[0:4])+' '+str(num[4:8])+' '+str(num[8:12])
            p.setFont('Helvetica-Bold', 18)
            p.drawString(x, y, line14)
            y=y-55
            p.drawInlineImage('left_b.PNG',31,y,width=253,height=50)
            p.drawInlineImage('right_b.PNG',300,y,width=253,height=50)
            p.setFont('Helvetica', 11)
            y=y-18
            line20=parse[3]+' '+parse[1]+' '+parse[2]
            p.drawString(x+20, y, line20)
            y=y-18
            line21='DOB:'+' '+str(parse[7])
            p.drawString(x+20, y, line21)
            y=y-50
            num = str(parse[0])
            p.setFont('Helvetica-Bold', 18)
            p.drawString(x+30, y, line14)
            year = str(parse[7])
            password = parse[3][0:4].upper()+year[0:4]
            print(password)
            encryptCanvas(p, password)
            p.showPage()
            p.save()
            return response
        else:
            return HttpResponse('No')

def find(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        mobile = request.POST['phone_num']
        uidai_cur.execute("SELECT phone FROM details")
        phonee = uidai_cur.fetchall()
        mobile = int(mobile)
        print(mobile)
        for phone in phonee:
            print(phone[0])
            if mobile == phone[0]:
                uidai_cur.execute("SELECT first_name,middle_name,last_name FROM details WHERE phone={}".format(mobile))
                name = uidai_cur.fetchone()
                full_name = name[0]+' '+name[1]+' '+name[2]
                print(full_name)
                print(fullname)
                if full_name == fullname:
                    smss = smsender()
                    otp = random.randint(100000,999999)
                    smss.send_sms(otp,mobile)
                    uidai_cur.execute("INSERT INTO verify_otp (phone_num,otp) VALUES ({},{})".format(mobile,otp))
                    uidai_cur.commit()
                    return render(request,"aadharcard/enter_otp_uid.html",{'phone_num':mobile})
                else:
                    return HttpResponse("Wrong information")
            else:
                continue
        return HttpResponse('The phone number is not registered')
    else:
        form = captcha()
    return render(request,'aadharcard/enter-name.html',{'form':form})

def otp_verify(request):
    if request.method == 'POST':
        mobile = request.POST['phone_num']
        otp = request.POST['otp']
        mobile = int(mobile)
        otp = int(otp)
        uidai_cur.execute("SELECT otp FROM verify_otp WHERE phone_num={}".format(mobile))
        num = uidai_cur.fetchone()
        print(otp)
        print(num[0])
        if otp == num[0]:
            uidai_cur.execute("DELETE FROM verify_otp WHERE otp={}".format(otp))
            uidai_cur.commit()
            uidai_cur.execute("SELECT aadhar_num FROM details where phone={}".format(mobile))
            uid = uidai_cur.fetchone()
            smss = smsender()
            mes = "Your aadharcard number is"+' '+str(uid[0])
            smss.send_sms(mes,mobile)
            return render(request,"aadharcard/Thankyou.html")
        else:
            return HttpResponse('Wrong otp')

'''
def aadhar_card(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "filename=narendra.pdf"
    p = canvas.Canvas(response)
    #encryptCanvas(p, "narendra")
    x=30
    y=9.5*72
    p.rect(30,3*72,255,8.5*72,stroke=1,fill=0)
    p.rect(300,3*72,254,8.5*72,stroke=1,fill=0)
    p.drawInlineImage('top.PNG',x,y,width=254,height=140)
    p.drawInlineImage('back.PNG',300,7.4*72,width=253,height=290)
    uidai_cur.execute('SELECT * FROM details WHERE aadhar_num={}'.format(560522624339))
    parse = uidai_cur.fetchone()
    p.setFont('Helvetica', 11)
    x=x+40
    y=y-22
    line3="Enrolment.no.:2017/78007/93872"
    p.drawString(x,y,line3)
    y=y-18
    line4=parse[3]+' '+parse[1]+' '+parse[2]
    p.drawString(x, y, line4)
    y=y-18
    line2='Gender:'+' '+parse[4]
    p.drawString(x, y, line2)
    y=y-18
    line5='S/O:'+' '+parse[5]
    p.drawString(x, y, line5)
    y=y-18
    line6='DO NO:'+' '+parse[11]
    p.drawString(x, y, line6)
    uidai_cur.execute('SELECT * FROM pincodes WHERE pincode={}'.format(parse[12]))
    det = uidai_cur.fetchone()
    y=y-18
    line8=det[1]
    p.drawString(x, y, line8)
    y=y-18
    line9=det[2]+' - '+str(det[0])
    p.drawString(x, y, line9)
    uidai_cur.execute('SELECT state FROM states WHERE id={}'.format(det[3]))
    state = .fetchone()
    y=y-18
    line10=state[0]
    p.drawString(x, y, line10)
    y=y-18
    line12=str(parse[9])
    p.drawString(x, y, line12)
    y=y-80
    line13="Your Aadhar number.:"
    p.drawString(x, y, line13)
    y=y-25
    num = str(parse[0])
    line14=str(num[0:4])+' '+str(num[4:8])+' '+str(num[8:12])
    p.setFont('Helvetica-Bold', 18)
    p.drawString(x, y, line14)
    y=y-55
    p.drawInlineImage('left_b.PNG',31,y,width=253,height=50)
    p.drawInlineImage('right_b.PNG',300,y,width=253,height=50)
    p.setFont('Helvetica', 11)
    y=y-18
    line20=parse[3]+' '+parse[1]+' '+parse[2]
    p.drawString(x+20, y, line20)
    y=y-18
    line21='DOB:'+' '+str(parse[7])
    p.drawString(x+20, y, line21)
    y=y-50
    num = str(parse[0])
    p.setFont('Helvetica-Bold', 18)
    p.drawString(x+30, y, line14)
    year = str(parse[7])
    encryptCanvas(p, password)
    password = parse[3][0:4].upper()+year[0:4]
    p.showPage()
    p.save()
    return response
'''
