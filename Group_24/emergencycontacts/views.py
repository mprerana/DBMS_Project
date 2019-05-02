from django.shortcuts import render,redirect
from emergencycontacts.models import *
from emergencycontacts.forms import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail, EmailMessage


from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.models import *
# Create your views here.

def emergencycontact(request):
    u = UserProfile.objects.get(user=request.user)
    emergency = Emergenycontactform(request.POST or None)
    if emergency.is_valid():
        emergencyinstance=emergency.save(commit=False)

        emergencyinstance.user = u
        emergencyinstance.save()
        return redirect('accounts:view_profile')
    else:
        emergency = Emergenycontactform()
    return render(request,'emergencycontacts/add.html',{'emergency':emergency})


def sendmail(request):
    u = UserProfile.objects.get(user=request.user)
    reciever = EmergencyContacts.objects.filter(user=u).first()
    if request.user.is_authenticated:
        username = request.user
    email = EmailMessage('Emergency', str(username)+' is in Danger ', to=[reciever.email,])
    email.send()
    return HttpResponse('<h1>Sent</h1>')
