from django.shortcuts import render
from account.forms import UserInfoForm ,QueryForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from login.models import UserProfileInfo
from django.conf import settings


from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.

from .forms import UserLoginForm,EditProfileForm


def index(request):
    return render(request,'index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    REGISTERED = False

    if request.method=='POST':

        user_info = UserInfoForm(request.POST)

        if user_info.is_valid() :

            user = user_info.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('login/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_info.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()

            REGISTERED=True
            return render(request,'login/registration_done.html')
        else:
            print(user_info.errors)
    else:

        user_info = UserInfoForm()

    return render(request,'login/register.html',{'user_info':user_info,'registered':REGISTERED})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.raw('SELECT * FROM auth_user WHERE id=%s',[uid])[0]
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return HttpResponse("activated")
        return redirect('/')

    else:
        return HttpResponse('Activation link is invalid!')


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect("/package/index")
    else:
        return render(request, "login/login.html", {"form": form})


@login_required(login_url='login')  # only logged in users should access this
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        old_email = user.email
        form = EditProfileForm(request.POST , instance=request.user)
        if form.is_valid():
            emails = form.cleaned_data.get('email')
            if emails != old_email:
                if User.objects.filter(email=emails):
                    return HttpResponse('email already exist')
                else:
                    user = request.user
                    user.is_active = False
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('login/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        'token': account_activation_token.make_token(user),
                    })
                    to_email = form.cleaned_data.get('email')
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()
                    form.save()
                    return render(request, 'login/edit_email_done.html')
            else:
                form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'login/editprofile.html', args)



def Queryview(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('your query is submitted')
    else:
        return render(request,'contact.html',{'form':QueryForm()})
