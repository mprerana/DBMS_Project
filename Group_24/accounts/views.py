from django.shortcuts import render,redirect
from accounts.forms import *
from rentedcars.forms import *
from rentedcars.models import *
from django.contrib.auth.models import User
from accounts.models import *

from geopy.geocoders import Nominatim

from django.contrib.auth import authenticate,login,logout

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'landing.html')


@login_required
def home(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        geolocator = Nominatim()
        car_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')
        form = BookingDetailForm(request.POST or None)
        if form.is_valid():
            u=UserProfile.objects.get(user=request.user)
            if u.user_type=='U':

                forminstance=form.save(commit=False)
                forminstance.user_booked=u
                forminstance.car_location=request.POST.get('from_location')
                forminstance.to_location=request.POST.get('to_location')
                forminstance.save()
                return redirect('rentedcars:display_avail_cars')
        return render(request,'home.html',{'form':form})
    elif u.user_type=='T':
        return redirect('accounts:taxi_home')
    elif u.user_type=='D':
        return render(request,'driverhome.html')


def user_signup(request):

    registered = False

    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.rating = '5'
            profile.save()


            registered = True
            print(profile.user_type)
            if profile.user_type=='T':
                return redirect('accounts:taxi_profile')
            else:
                return redirect('accounts:user_login')
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'accounts/signup.html',
                {'user_form':user_form,
                'profile_form':profile_form,
                'registered':registered})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('accounts:home')
            else:
                return HttpResponse("accounts not active")
        else:
            print("someone tried to login failed")
            return HttpResponse("invalid details")
    else:
        return render(request,'accounts/login.html',{})



@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')


@login_required
def taxi_home(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='T':
        t=TaxiProfile.objects.get(user=u)
        if request.method =='POST':
            for key in request.POST.items():
                if key[0] == 'active':
                    t.active=False
                    t.save()
                if key[0] == 'inactive':
                    t.active=True
                    t.save()
        return render(request,'taxihome.html',{'t':t})




def taxi_profile(request):
    geolocator = Nominatim()
    if request.method == 'POST':
        location = request.POST.get('location')
        taxi_num = request.POST.get('taxi_num')
        taxi_name = request.POST.get('taxi_num')
        price = request.POST.get('price')
        # u=UserProfile.objects.raw(" select *from accounts_userprofile ORDER BY auto_increment_id DESC LIMIT 1")
        u=UserProfile.objects.all().last()
        if u.user_type=='T':
            TaxiProfile.objects.create(location=location,taxi_num=taxi_num,taxi_name=taxi_name,price=price,active=True,user=u,is_booked=False)
            return redirect('accounts:user_login')
    return render(request,'accounts/taxi_details.html')

# @login_required
# def driver_profile(request):
#
#     if request.method == 'POST':
#         driver_form=DriverProfileForm(request.POST)
#
#         if taxi_form.is_valid():
#             u=UserProfile.objects.get(user=request.user)
#
#             driverform = driver_form.save(commit=False)
#             driverform.active = True
#             driverform.user=u
#             driverform.is_booked=False
#             driverform.save()
#
#
#     else:
#         user_form=TaxiProfileForm()
#
#     return render(request,'accounts/driver_detail.html',
#                 {'driver_form':driver_form,})


@login_required
def view_profile(request):
    u= UserProfile.objects.get(user=request.user)
    user=request.user
    if u.user_type == 'U':
        args={'user':user,'u':u,}
        return render(request,'accounts/user_profile.html',args)
    elif u.user_type == 'T':
        t=TaxiProfile.objects.get(user=u)
        taxi = TaxiProfile.objects.get(user=u)
        args = {'user':user,'u':u,'taxi':taxi,'t':t}
        return render(request,'accounts/taxi_profile.html',args)
