from django.shortcuts import render,redirect
from userlogin.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from userlogin.models import Profile
from .forms import UserRegisterForm, EditProfileForm, UserProfileForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm , PasswordChangeForm
# Create your views here.
def index(request):
    # Create your views here.

    return render(request, "userlogin/index.html")

def signup(request):
    # Create your views here.
    if request.method=='POST':

        form=UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            new_user = form.save(commit=False)
            new_user.is_active=False
            new_user.save()
            new_user.refresh_from_db()  # load the profile instance created by the signal
            new_user.save()
            city = form.cleaned_data.get('city')
            address= form.cleaned_data.get('address')
            phone_number = form.cleaned_data.get('phone_number')
            pincode=form.cleaned_data.get('pincode')
            country = form.cleaned_data.get('country')
            picture = form.cleaned_data.get('picture')
            profile=Profile()
            profile.user = new_user




            profile.phone_number = phone_number
            profile.address = address
            if picture:
                profile.picture = picture
            profile.country = country
            profile.pincode=pincode
            profile.city=city
            profile.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your Donatekart account.'
            message = render_to_string('userlogin/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)).decode(),
                'token':account_activation_token.make_token(new_user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')


        print(form)
    else:
        form = UserRegisterForm()
        print(form)

    return render(request, "userlogin/signup.html",{'form':form})

def edit_profile(request):
    if request.method == 'POST':
        passform = PasswordChangeForm(request.user, request.POST)
        user_form = EditProfileForm(request.POST,instance=request.user)
        print(user_form)
        profile_form = UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            print(user_form)
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('user_login:user_login.edit_profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        print('outside')
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
        passform = PasswordChangeForm(request.user, request.POST)

    return render(request, 'userlogin/profile_edit2.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'passform':passform,
            'user':request.user
        })
        
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login.view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'userlogin/change_password.html', {
        'form': form
    })

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed=True
        user.save()
        user.profile.save()

        login(request, user)
        return redirect(reverse('userlogin:userlogin.edit_profile'))

    else:
        return HttpResponse('Activation link is invalid!')
