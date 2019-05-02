from django.shortcuts import render,redirect
from weddingcars.models import *
from notifications.models import *

from geopy.geocoders import Nominatim

from django.utils import timezone

# Create your views here.

def weddingcardisplay(request):
    cars=WeddingCar.objects.raw("CALL Getweddingcars()")
    # cars = WeddingCar.objects.filter(is_booked=False)
    return render(request,'weddingcars/weddingcars_home.html',{'cars':cars})


def weddingcar_book(request,wed_id):
    u=UserProfile.objects.get(user=request.user)
    item = WeddingCar.objects.get(pk = wed_id)
    item.is_booked=True
    item.save()

    geolocator = Nominatim()
    from_location = request.POST.get('from_location')
    print(from_location)
    to_location = request.POST.get('to_location')
    print(to_location)
    BookedWeddingCar.objects.create(user_booked=u,from_location=from_location,to_location=to_location,wedding_car=item,booked_date=timezone.now().date())
    NotificationList.objects.create(message='you have booked a wedding car',read=False,user=u)
    return redirect('weddingcars:weddingcardisplay')

def display_map(request,map_id):
    u=UserProfile.objects.get(user=request.user)
    trip = BookedWeddingCar.objects.get(pk = map_id)
    return render(request,'weddingcars/each_history.html',{'trip':trip})


def tourists_view_history(request):
    u=UserProfile.objects.get(user=request.user)
    all_trips = BookedWeddingCar.objects.all()
    return render(request,'weddingcars/weddingcars_history.html',{'all_trips':all_trips,'u':u})
