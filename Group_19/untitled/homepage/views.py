from django.shortcuts import render
from homepage.forms import UserForm,FeedbackForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from homepage.models import feedback
from django.shortcuts import redirect
from django.db import connection
cursor=connection.cursor()
from homepage.models import UserProfileInfo
from collections import namedtuple
from credits.models import *

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
def index(request):


    return render(request,'homepage/index.html')

def video_chat(request):
    return render(request,'events/video_chat.html')

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        re_password=request.POST.get('re_password')
        password=request.POST.get('password')
        username=request.POST.get('username')
        email=request.POST.get('email')

        print(password,"\n",re_password)
        if re_password==password:
            if user_form.is_valid():
                user=user_form.save()
                user.set_password(user.password) #hashing the password
                user.save() #save hash password to database
                registered=True
                AccountBalance.objects.create(user=user, balance=100)
                user = authenticate(username=username, password=password)
                id=User.objects.get(username=user.username).pk
                print("going")


            else:
                print("something is fishy")
        else:

            raise forms.ValidationError("Passwords do not match.Please Re_enter them")

            raise forms.ValidationError("Passwords do not match")

    else:
        user_form=UserForm()

    return render(request,'homepage/registration.html',{'user_form':user_form,'registered':registered,})

@login_required
def special(request):
    return HttpResponse("You are logged in dude")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print("username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'homepage/login.html')
def user_feedback(request):
    if request.method=="POST":
        feedback_form=FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback=feedback_form.save()
            feedback.save()
            print(feedback_form.cleaned_data['text'])
        return HttpResponseRedirect(reverse('index'))
    return render(request,'homepage/feedback.html')
def display_feedback(request):
    feedbacks=feedback.objects.order_by('-pk')

    sum=0
    count=0
    for i in feedbacks:
        sum=sum+int(i.rating)
        count=count+1
    avg_rating=sum/count

    my_dict={'feedbacks':feedbacks,'avg_rating':avg_rating}
    return render(request,'homepage/display_feedbacks.html',my_dict)

def earn_rent(request,value):
    info_object, created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name=request.user.username
    user_id=User.objects.get(username=request.user.username).pk
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND p_id=%s """ % (user_id,value))
    cost = cursor.fetchone()[5]
    if cost==0:
        cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND p_id=%s """ % (user_id, value))
        area=cursor.fetchone()[2]
        cost=area*125*30
    a='rent'

    cursor.execute("UPDATE plot_details SET Available_for='rent', cost=%s WHERE p_id=%s " % (cost/30,value))


    return redirect('homepage:profile_view')

def sell_this(request,value):
    info_object, created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name=request.user.username
    user_id=User.objects.get(username=request.user.username).pk
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND p_id=%s """ % (user_id,value))
    cost = cursor.fetchone()[5]
    if cost==0:
        cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND p_id=%s """ % (user_id, value))
        area=cursor.fetchone()[2]
        cost=area*125
    a='buy'

    cursor.execute("UPDATE plot_details SET Available_for='buy', cost=%s WHERE p_id=%s " % (cost*30,value))


    return redirect('homepage:profile_view')

def remove_this(request,value):
    info_object, created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name=request.user.username
    user_id=User.objects.get(username=request.user.username).pk
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND p_id=%s """ % (user_id,value))
    cost = cursor.fetchone()[5]

    cursor.execute("UPDATE plot_details SET Available_for='shop', cost=%s WHERE p_id=%s " % (0,value))


    return redirect('homepage:profile_view')




def profile_view(request):

    info_object,created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name = request.user.username
    user_id = User.objects.get(username=request.user.username).pk

    a='shop'
    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND Available_for='buy' """ % (user_id))
    buy=namedtuplefetchall(cursor)




    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND Available_for='rent' """ % (user_id))
    rent=namedtuplefetchall(cursor)


    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND Available_for='shop' """ % (user_id))
    shop=namedtuplefetchall(cursor)

    cursor.execute("""SELECT * FROM plot_details WHERE admin_id=%s AND tenant_id IS NOT NULL  """ % (user_id))
    tenant_plots = namedtuplefetchall(cursor)

    cursor.execute("""SELECT * FROM plot_details WHERE admin_id<>%s AND tenant_id=%s  """ % (user_id,user_id))
    my_rented_plots = namedtuplefetchall(cursor)
    print(my_rented_plots)
    my_dict = {'my_rented_plots': my_rented_plots,'tenant_plots':tenant_plots,'shop':shop,'buy':buy,'rent':rent,'user': user_name,  'bio': info_object.bio, 'phone': info_object.phone,'city': info_object.city}
    return render(request,'homepage/user_profile.html', my_dict)

def edit_profile(request):
    if request.method=="POST":
        bio=request.POST.get('bio')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        user=request.user
        info_object,created=UserProfileInfo.objects.get_or_create(user=user)
        info_object.bio=bio
        info_object.phone=phone
        info_object.city=city
        info_object.save()

        user_name = request.user.username
        print(user_name)

        my_dict = {'user': user_name, 'bio':info_object.bio,'phone':info_object.phone,'city':info_object.city}
        return render(request, 'homepage/user_profile.html', my_dict)
    return render(request,'homepage/edit_profile.html')







