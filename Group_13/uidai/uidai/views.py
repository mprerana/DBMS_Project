from django.http import HttpResponse
from django.shortcuts import render,redirect
#from service.forms import Complaint_Check_Form
from service.sms import Sms
from django.core.mail import send_mail
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import pyodbc

uidai_con = pyodbc.connect("DRIVER={SQL Server};SERVER=10.0.33.62,1433;DATABASE=uidai;UID=uidai;PWD=uidai")
uidai_cur = uidai_con.cursor()

def nearest_centre(request):
    return render(request,'nearestcentres.html')

def test(request):
    if request.method == "POST":
        eid = uidai_cur.execute("SELECT [dbo].[eid_generate]();").fetchall()[0][0]
        details = request.POST
        fname = details['fname']
        mname = details['mname']
        lname = details['lname']
        faname = details['faname']
        moname = details['moname']
        ph = details['phone_no']
        email = details['email']
        bpl = details['birthplace']
        res = details['res_addr']
        city = details['city']
        pincode = details['pincode']
        state = details['state']
        dist = details['dist']
        country = details['country']
        dob = details['dob']
        gender = details['gender']
        uidai_cur.execute("EXEC add_new_entry @fname = '{}', @mname = '{}', @lname = '{}', @gender = '{}', @faname = '{}', @moname = '{}', @dob = '{}', @birthplace = '{}', @p_no = {}, @email = '{}', @address = '{}', @city = '{}', @district = '{}', @state = '{}', @pincode = {}, @country = '{}', @enloc = '{}', @eid = {};".format(fname, mname, lname, gender, faname, moname, dob, bpl, ph, email, res,  city, dist, state, pincode, country, 1, eid))
        uidai_cur.commit()
        return redirect('/test/')
    return render(request, 'form.html')

def uidai_home(request):
    return render(request, 'homepage.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # request check for complaints/address update
            return redirect('address_update_check')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')

@login_required(login_url="/login/")
def complaint_check(request):
    if request.user.groups.filter(name ='admin').exists():
        if 'complaint_type' in request.POST:
            complaint_type = request.POST['complaint_type']

            #uidai_cur = connection.uidai_cur()
            uidai_cur.execute("SELECT complaint_id, aadhar_num, user_name, category FROM complaints WHERE EXISTS (SELECT complaint_id FROM complaint_status WHERE complaint_id = complaints.complaint_id AND status = '{}' AND category= {})".format("In Progress", complaint_type))
            all_complaints = uidai_cur.fetchall()

            context = {'all_complaints':all_complaints}
            print(all_complaints)

            return render(request, 'complaint_check.html', context)
        else:
            #uidai_cur = connection.uidai_cur()
            uidai_cur.execute("SELECT complaint_id, aadhar_num, user_name, category FROM complaints WHERE EXISTS (SELECT complaint_id FROM complaint_status WHERE complaint_id = complaints.complaint_id AND status = '{}')".format("In Progress"))      # still need to check the status, Authentication
            all_complaints = uidai_cur.fetchall()
            print(all_complaints)

            return render(request, 'complaint_check.html', {'all_complaints':all_complaints})
    else:
        return HttpResponse("you dont have privilage to check")

@login_required(login_url="/login/")
def complaint_reply(request, id):
    if request.user.groups.filter(name ='admin').exists():
        if request.method == 'POST':
            reply = request.POST['reply']
            print(reply)
            #uidai_cur = connection.uidai_cur()
            uidai_cur.execute("UPDATE complaint_status SET reply='{}', status='{}' WHERE complaint_id = {}".format(reply, "success", id))

            #send_sms = Sms('9121587454','Shiva@01')
            #send_sms.send(phone_no, 'Your complaint ID:'+ str(complaint_id) + ",please verify your complaint status with this id")

            return redirect('complaint_check')
        return  render(request, 'complaint_reply.html', {'id':id})
    else:
        return HttpResponse("you dont have privilage to reply")


@login_required(login_url="/login/")
def address_update_check(request):
    if request.user.groups.filter(name ='admin').exists():
        if 'address_proof' in request.POST:
            address_proof = request.POST['address_proof']

            # uidai_cur = connection.uidai_cur()
            uidai_cur.execute("SELECT aadhar_num, proof_type FROM document WHERE proof_type='{}'".format(address_proof))
            details_proof = uidai_cur.fetchall()
            context = {'details_proof':details_proof}

            return render(request, 'address_update_check.html', context)
        else:
            #uidai_cur = connection.uidai_cur()
            uidai_cur.execute("SELECT aadhar_num,proof_type FROM document")
            details_proof = uidai_cur.fetchall()

            context = {
                'details_proof': details_proof,
            }
            return render(request, 'address_update_check.html', context)
    else:
        return HttpResponse("You dont have privilage to check")

@login_required(login_url="/login/")
def address_update_check_reply(request, id):
    #uidai_cur = connection.uidai_cur()
    uidai_cur.execute("SELECT * FROM update_req INNER JOIN document ON document.aadhar_num = {};".format(id))
    details_documents = uidai_cur.fetchall()
    if request.method == "POST":
        if 'Accept' in request.POST:
            uidai_cur.execute("SELECT * FROM update_req WHERE aadhar_num = {};".format(id))
            updating_address = uidai_cur.fetchall()
            print(updating_address)
            add = str(updating_address[0][2]) + str(updating_address[0][3]) + str(updating_address[0][4]) + str(updating_address[0][5])

            uidai_cur.execute("UPDATE details SET res_address='{}', pincode={} WHERE aadhar_num = {}".format(add,updating_address[0][6], id))
            uidai_cur.execute("UPDATE update_status SET address_status='{}' WHERE aadhar_num = {}".format("Accepted", id))
            uidai_cur.execute("DELETE FROM update_req WHERE aadhar_num={}".format(id))
            uidai_cur.commit()
            uidai_cur.execute("DELETE FROM document WHERE aadhar_num={}".format(id))
            uidai_cur.commit()

            send_sms = Sms('9121587454','Shiva@01')
            send_sms.send(phone_no, "your address on aadhar has been updated")
            return redirect('address_update_check')

        if 'Reject' in request.POST:
            uidai_cur.execute("DELETE FROM update_req WHERE aadhar_num={}".format(id))
            uidai_cur.commit()
            uidai_cur.execute("DELETE FROM document WHERE aadhar_num={}".format(id))
            uidai_cur.commit()
            uidai_cur.execute("UPDATE update_status SET address_status='{}' WHERE aadhar_num = {}".format("Rejected", id)) #function
            # phone_no
            #send_sms = Sms('9121587454','Shiva@01')
            #send_sms.send(phone_no, "your request for aadhar address update was rejected")

            return redirect('address_update_check')

    return render(request, 'address_update_check_reply.html', {'id':id,'details':details_documents})
