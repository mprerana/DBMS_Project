from django.shortcuts import render,redirect
from taxis.forms import *
from taxis.models import *
from notifications.models import *
from accounts.models import *
from rentedcars.models import *
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim

import datetime

# Create your views here.

@login_required
def booktaxi(request):
    geolocator = Nominatim()
    if request.method == 'POST':
        from_location = request.POST.get('from_location_taxi')
        to_location = request.POST.get('to_location_taxi')
        u=UserProfile.objects.get(user=request.user)
        if u.user_type=='U':
            TaxiBooking.objects.create(user_booking=u,date=timezone.now().date(),from_location=from_location,to_location=to_location)
            return redirect('taxis:avail_taxi')
    return redirect('accounts:home')


@login_required
def avail_taxi(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        details=TaxiBooking.objects.filter(user_booking=u).last()
        taxi = TaxiProfile.objects.filter(location=details.from_location,active=True)
    return render(request,'taxis/avail_taxi.html',{'taxi':taxi})

@login_required
def accept_taxi(request,accept_id):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        item = TaxiProfile.objects.get(pk = accept_id)
        details=TaxiBooking.objects.filter(user_booking=u).last()
        BookedTaxi.objects.create(taxi_booking_details=details,taxi_booked=item,time=timezone.now().time(),active=True)
        NotificationList.objects.create(message='Taxi is booked',read=False,user=u)
    return redirect('accounts:home')

#
# @login_required
# def all_trips(request):
#     u= UserProfile.objects.get(user=request.user)
#     if u.user_type=='U':
#         return render(request,'taxis/mytrip.html')

@login_required
def your_trip(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        # mytrip=BookedTaxi.objects.raw("CALL Getbookedtaxitrips()")
        mytrip=BookedTaxi.objects.filter(active=True)
    return render(request,'taxis/trip.html',{'mytrip':mytrip,'u':u,})


@login_required
def endtrip(request,end_id):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        item = BookedTaxi.objects.get(pk = end_id)
        item.active=False
        item.save()
        t = TaxiProfile.objects.get(pk=item.taxi_booked.pk)
        t.location=item.taxi_booking_details.to_location
        t.save()

        rating=request.POST.get('rating')
        taxi_driver = UserProfile.objects.get(user=item.taxi_booked.user.user)
        print(taxi_driver)
        taxi_driver.rating=rating
        print(rating)
        print(taxi_driver.rating)
        taxi_driver.save()
        NotificationList.objects.create(message='you have ended your trip',read=False,user=u)
    return redirect('accounts:home')




@login_required
def book_driver(request):
    u =UserProfile.objects.get(user=request.user)
    if u.user_type == 'U':
        geolocator = Nominatim()
        if request.method == 'POST':
            location = request.POST.get('location_driver')
            drivers = DriverProfile.objects.filter(location=location,is_booked=False,active=True)
            return render(request,'taxis/drivers.html',{'drivers':drivers})


@login_required
def book_d(request,driver_id):
    u =UserProfile.objects.get(user=request.user)
    item = DriverProfile.objects.get(pk = driver_id)
    item.is_booked = True
    item.save()

    BookedDriver.objects.create(user_booked = u,driver = item,date =timezone.now().date())
    NotificationList.objects.create(message='booked a driver',read=False,user=u)
    return redirect('accounts:home')

@login_required
def display_map(request,map_id):
    u=UserProfile.objects.get(user=request.user)
    trip = BookedTaxi.objects.get(pk = map_id)
    return render(request,'taxis/each_history.html',{'trip':trip})


@login_required
def taxi_view_history(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type == 'T':
        t=TaxiProfile.objects.get(user=u)
        all_trips = BookedTaxi.objects.filter(taxi_booked=t)
        return render(request,'taxis/taxi_history.html',{'all_trips':all_trips,})
    elif u.user_type == 'U':
        t=TaxiBooking.objects.filter(user_booking=u).last()
        all_trips=BookedTaxi.objects.filter(taxi_booking_details=t)
        return render(request,'taxis/user_history.html',{'all_trips':all_trips,})
