from django.shortcuts import render,HttpResponse
from django.db import connection
from django.core.mail import send_mail

import pyodbc

app_name = 'history'

uidai_con = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.33.62,1433;DATABASE=uidai;UID=uidai;PWD=uidai")
uidai_cur = uidai_con.cursor()
cursor = connection.cursor()

frm_uidai  = {'A': 'phone', 'B': 'res_address', 'C': 'date_of_birth', 'D': 'first_name'}
from_cus = {'a': 'phone_no', 'b': 'address', 'c': 'date_of_birth', 'd': 'academic_details', 'e': 'voter_id_details', 'f': 'aadhar_details', 'g': 'license', 'h': 'ration_details', 'i': 'pan_card_details', 'j': 'caste_cert', 'k': 'bank_details'}

def get_history(request):
    if request.method == "POST":
        anum = request.POST['aadhar_num']
        uidai_cur.execute("SELECT * FROM update_history where aadhar_num = "+str(anum))
        details = uidai_cur.fetchall()
        context = {'details': details}
        # for row in details:
        #     pincode = row[9]
        #     uidai_cur.execute("select * from pincodes where pincode = " + str(pincode))
        #     sta = uidai_cur.fetchall()
        #     uidai_cur.execute("select * from states where id = " + str(sta[0][3]))
        #     state = uidai_cur.fetchall()
        #     context['details'].append(row)
        return render(request, 'history.html', context)
    else:
        return render(request, 'anum.html')

def ServiceRegister(request):
    return render(request, 'ServiceRegister.html')




def validation(request):
    if request.method == "POST":
        details = request.POST
        dat = details
        service = request.POST["service_name"]
        administrator = request.POST["Administrator"]
        email = request.POST["email"]
        phone = request.POST["ContNo"]
        description = request.POST["desc"]
        uidai_cur.execute("INSERT INTO services(name, administrator_name, email, phone_no, description) VALUES ('{}', '{}', '{}', {}, '{}');".format(service, administrator, email, phone, description))
        uidai_cur.commit()
        sid = uidai_cur.execute("SELECT servicce_id from services where name='{}'".format(service)).fetchall()[0][0]
        print(sid)
        dat._mutable = True
        dat.pop('desc', None)
        dat.pop('ContNo', None)
        dat.pop('email', None)
        dat.pop('Administrator', None)
        dat.pop('service_name', None)
        dat.pop('csrfmiddlewaretoken', None)
        print('hello',dat)

        for key in dat:
            try:
                kd = frm_uidai[key]
                uidai_cur.execute("INSERT INTO service_needs(service_id, what_to) VALUES({}, '{}');".format(sid, kd))
                uidai_cur.commit()
            except:
                pass
            try:
                kd = from_cus[key]
                uidai_cur.execute("INSERT INTO cus_needs(service_id, cus_needs) VALUES({}, '{}');".format(sid, kd))
                uidai_cur.commit()
            except:
                pass

        data = "Hello {}. Your registration for {}'s service is successful.Please not your servie id for accessing details. It is {}. ".format(administrator, service, sid)
        #send_mail(data,'ruthala.shiva5128@gmail.com',['ruthala.shiva5128@gmail.com'],fail_silently=False,)
        return redirect("{% url 'http://10.0.39.17:8000/' %}")
    else:
        return render(request, 'ServiceRegister.html')
