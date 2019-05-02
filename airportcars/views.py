from django.shortcuts import render,redirect
from accounts.models import *
from airportcars.models import *
from notifications.models import *

from geopy.geocoders import Nominatim
from django.utils import timezone


def bookairportcar(request):
    u=UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        for key in request.POST.items():
            if key[0] == 'from_airport':
                cars=AirportCar.objects.raw("CALL Getfromairport()")
                # cars=AirportCar.objects.filter(from_airport=True,is_booked=False)
            if key[0] == 'to_airport':
                cars=AirportCar.objects.raw("CALL Gettoairport()")
                # cars=AirportCar.objects.filter(from_airport=False,is_booked=False)
        return render(request,'airportcars/display.html',{'cars':cars})
    return redirect('accounts:home')


def book_a_car(request,air_id):
    u=UserProfile.objects.get(user=request.user)
    item = AirportCar.objects.get(pk = air_id)
    item.is_booked=True
    item.save()
    geolocator = Nominatim()
    location = request.POST.get('location')
    if item.from_airport == True:
        BookedAirportCar.objects.create(user_booked=u,from_location='Chennai International Airport (MAA), GST Rd, Meenambakkam, Chennai, Tamil Nadu',to_location=location,airport_car=item,date=timezone.now().date())
    elif item.from_airport == False:
        BookedAirportCar.objects.create(user_booked=u,from_location=location,to_location='Chennai International Airport (MAA), GST Rd, Meenambakkam, Chennai, Tamil Nadu',airport_car=item,date=timezone.now().date())
        NotificationList.objects.create(message='airport service car is booked to airport',read=False,user=u)
    return redirect('airportcars:bookairportcar')


def display_map(request,map_id):
    u=UserProfile.objects.get(user=request.user)
    trip = BookedAirportCar.objects.get(pk = map_id)
    return render(request,'airportcars/each_histroy.html',{'trip':trip})


def tourists_view_history(request):
    u=UserProfile.objects.get(user=request.user)
    all_trips = BookedAirportCar.objects.all()
    return render(request,'airportcars/airportcars_history.html',{'all_trips':all_trips,'u':u})
