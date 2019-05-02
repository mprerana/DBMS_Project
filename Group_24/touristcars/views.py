from django.shortcuts import render,redirect
from accounts.models import *
from touristcars.models import *
from notifications.models import *
from django.utils import timezone

from geopy.geocoders import Nominatim


def booktour(request):
    u=UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        for key in request.POST.items():
            if key[0] == 'place1':
                 # SELECT * FROM touristcars_touristcar WHERE to_location='MGR Memorial, Marina Beach Road, Navalar Nagar, Chepauk, Triplicane, Chennai, Tamil Nadu' AND is_booked='0';
                # tours=TouristCar.objects.filter(to_location='MGR Memorial, Marina Beach Road, Navalar Nagar, Chepauk, Triplicane, Chennai, Tamil Nadu',is_booked=False)
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='MGR Memorial, Marina Beach Road, Navalar Nagar, Chepauk, Triplicane, Chennai, Tamil Nadu' AND is_booked='0'")
            if key[0] == 'place2':
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='Queensland, Chennai, Tamil Nadu, India' AND is_booked='0'")
                # tours=TouristCar.objects.filter(to_location='Queensland, Chennai, Tamil Nadu, India',is_booked=False)
            if key[0] == 'place3':
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='Guindy National Park, Chennai, Tamil Nadu, India' AND is_booked='0'")
                # tours=TouristCar.objects.filter(to_location='Guindy National Park, Chennai, Tamil Nadu, India',is_booked=False)
            if key[0] == 'place4':
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='Mahabalipuram, Tamil Nadu' AND is_booked='0'")
                # tours=TouristCar.objects.filter(to_location='Mahabalipuram, Tamil Nadu',is_booked=False)
            if key[0] == 'place5':
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='Marina Beach, Chennai, Tamil Nadu' AND is_booked='0'")
                tours=TouristCar.objects.filter(to_location='Marina Beach, Chennai, Tamil Nadu',is_booked=False)
            if key[0] == 'place6':
                tours=TouristCar.objects.raw("SELECT * FROM touristcars_touristcar WHERE to_location='Muttukadu, Tamil Nadu' AND is_booked='0'")
                # tours=TouristCar.objects.filter(to_location='Muttukadu, Tamil Nadu',is_booked=False)
        return render(request,'touristcars/display.html',{'tours':tours})
    return render (request,'touristcars/tourist.html',)


def booktourcar(request,tour_id):
    u=UserProfile.objects.get(user=request.user)
    item = TouristCar.objects.get(pk = tour_id)
    item.is_booked=True
    item.save()
    geolocator = Nominatim()
    location = request.POST.get('to_location')
    BookedTourCar.objects.create(user_booked=u,from_location=location,tour_car=item,date=timezone.now().date())
    NotificationList.objects.create(message='you have booked a tourist car',read=False,user=u)
    return redirect('touristcars:booktour')

def display_map(request,map_id):
    u=UserProfile.objects.get(user=request.user)
    trip = BookedTourCar.objects.get(pk = map_id)
    return render(request,'touristcars/each_history.html',{'trip':trip})


def tourists_view_history(request):
    u=UserProfile.objects.get(user=request.user)
    all_trips = BookedTourCar.objects.all()
    return render(request,'touristcars/touristcars_history.html',{'all_trips':all_trips,'u':u})
