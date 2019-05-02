import random
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import profile_form, LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from rest_framework.views import APIView
import psycopg2
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .models import *
from rest_framework import status
from registration.tokens import account_activation_token
conn=psycopg2.connect(host="127.0.0.1", database="blog", user="postgres", password="password")
from .serializers import userSerializer

class SignUpView(APIView):
    def get(self, request):
        int1 = User.objects.all()
        serializer = userSerializer(int1,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print(data)
        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password1']
        username_error=''
        email_error = ''
        password_error = ''
        password2_error = ''
        error = False
        if username=='':
            error=True
            username_error="Username can't be empty"
        if error==False:
            user_set = User.objects.filter(username=username)
            if len(user_set)>0:
                error=True
                username_error="Username already exists"
        if email == '':
            error = True
            email_error = "Email can't be empty"
        if password == '':
            error = True
            password_error = "Password can't be empty"
        if password != password2:
            error = True
            password2_error = "Passwords didn't match"
        if error==False:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            )
            user.set_password(password)
            user.is_active = False
            user.save()
            mail = email
            print(mail)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            send_mail(mail_subject, message, 'iiits2021@gmail.com', [mail])

        errors = {'username_error':username_error,'email_error':email_error,'password_error':password_error,'password2_error':password2_error,'error':error}
        print(errors)
        return Response(errors)
class SignInView(APIView):
    def get(self, request):
        int1 = User.objects.all()
        serializer = userSerializer(int1,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print(data)
        username = data['username']
        password = data['password']
        username_error=''
        password_error = ''
        error = False
        if username=='':
            error=True
            username_error="Username can't be empty"
        if error==False:
            user_set = User.objects.filter(username=username)
            if len(user_set)==0:
                error=True
                username_error="Username does not exist"
        if password == '':
            error = True
            password_error = "Password can't be empty"
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print(request.user)
                return redirect('http://127.0.0.1:8080/')
        else:
            error = True
            password_error = "Invalid password"

        errors = {'username_error':username_error,'password_error':password_error,'error':error}
        print(errors)
        return Response(errors)




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        Bookmark.objects.create(user=user)
        profile.objects.create(user=user)
        Follower.objects.create(follower=user)
        return redirect('http://127.0.0.1:8080/')
    else:
        return HttpResponse('Activation link is invalid!')






'''useless'''






@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



def edit_profile(request):
    user = request.user


    form=profile_form(request.POST, request.FILES)
    

    if form.is_valid():

        user_data=form.cleaned_data
        curr = conn.cursor()
        curr.execute("INSERT INTO registration_profile (user_id, fullname,gender, age,phone_no) VALUES (%d, %s, %s, %s,%s)",(user.id ,user_data['fullname'], user_data["gender"], user_data["age"],user_data["phone_no"]))

        conn.commit()
        return redirect(reverse('registration:show_profile'))       

    else:
        form=profile_form()


    return render(request, 'registration/modify_profile.html', {"form": form})


def show_profile(request):
  
    user = request.user
    user_id=user.id
    curr = conn.cursor()
    curr.execute("SELECT * FROM registration_profile WHERE user_id= %s", [user_id])
    row=curr.fetchone()
    print(row)
    return render(request,'registration/show_profile.html', {'profile':row })
  
  


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user.is_authenticated)
            login(request, user)
            return redirect(reverse('registration:show_profile'))
        else:
            print("User is none")

    return render(request, "registration/login.html", context=context)


def email_verify(form):
    rand_numb = random.randint(10000, 999999)
    global b
    b = str(rand_numb)
    email = [form.data['email']]
    response = send_mail("OTP for registration", b, "smarthealthcaresystemiiits@gmail.com", email)
    return b


# User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            b = email_verify(form)
            print(b)
            username = form.data['username']
            email = form.data['email']
            password = form.data['password']
            context = {
                'username': username,
                'email': email,
                'password': password,
                'b': b,
            }

            return render(request, 'registration/verify.html', context)
    else:
        form = RegisterForm()
        messages.error(request, 'Invalid login credentials')
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


# User = get_user_model()
def new_user_reg(request):
    if b == request.POST['token']:
        if request.method == 'POST':
            username = request.POST.get('username', False)
            email = request.POST.get('email', False)
            password = request.POST.get('password', False)
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(request.POST['password'])
            new_user.save()
            login(request, new_user)
            print(new_user)
            return redirect('/users/edit_profile')
    else:
        return HttpResponse('Please give correct OTP')


def log_out(request):
    logout(request)

    return redirect('/')


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
