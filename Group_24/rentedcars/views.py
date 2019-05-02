from django.shortcuts import render,redirect
from rentedcars.forms import *
from rentedcars.models import *
from notifications.models import *
from accounts.models import *
from django.contrib.auth import authenticate,login,logout
from geopy.geocoders import Nominatim

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rentcardisplay(request):
    u=UserProfile.objects.get(user=request.user)

    if u.user_type=='U':
        rented_cars = RentedCar.objects.filter(user_rented=u)
        return render(request, 'rentedcars/rentcardisplay.html',{'rented_cars':rented_cars})
    else:
        return HttpResponse("not a valid user")

@login_required
def rentcarform(request):
    geolocator = Nominatim()
    car_location = request.POST.get('car_location')
    detailsform = CarDetailForm(request.POST or None, request.FILES or None)
    form = RentedCarForm(request.POST or None)
    if form.is_valid() and detailsform.is_valid():
        u=UserProfile.objects.get(user=request.user)
        if u.user_type=='U':

            detailsforminstance=detailsform.save(commit=False)
            detailsforminstance.save()

            forminstance=form.save(commit=False)
            forminstance.user_rented=u
            forminstance.car_location=car_location
            forminstance.car_details=detailsforminstance
            forminstance.is_booked=False
            forminstance.save()
            NotificationList.objects.create(message='you have succesfully rented your car with num '+str(forminstance.car_details.car_num),read=False,user=u)
        return redirect('rentedcars:rentcardisplay')
    return render(request,'rentedcars/rentcarform.html' ,{'detailsform':detailsform,'form':form,})


# @login_required
# def bookcabform(request):
#     geolocator = Nominatim()
#     car_location = request.POST.get('car_location')
#     to_location = request.POST.get('to_location')
#     form = BookingDetailForm(request.POST or None)
#     if form.is_valid():
#         u=UserProfile.objects.get(user=request.user)
#         if u.user_type=='U':
#
#             forminstance=form.save(commit=False)
#             forminstance.user_booked=u
#             forminstance.to_location=request.POST.get('to_location')
#             forminstance.car_location=request.POST.get('car_location')
#             forminstance.save()
#             return redirect('rentedcars:display_avail_cars')
#     return render(request,'rentedcars/form_book.html' ,{'form':form})


@login_required
def display_avail_cars(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        details=BookingDetail.objects.filter(user_booked=u).last()
        cars_avail = RentedCar.objects.filter(car_location=details.car_location,from_date=details.from_date,to_date=details.to_date,is_booked=False)
        return render(request,'rentedcars/display_avail_cars.html' ,{'cars_avail':cars_avail,'u':u,})

@login_required
def book_my_car(request,book_id):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        details=BookingDetail.objects.filter(user_booked=u).last()
        item = RentedCar.objects.get(pk = book_id)
        if details.user_booked != item.user_rented:
            BookedCar.objects.create(car_rented=item,booking_Details=details,accept=False,active=False,date=timezone.now().date())
            NotificationList.objects.create(message='you have succesfully requested user '+str(item.user_rented.user),read=False,user=u)
            NotificationList.objects.create(message='you have succesfully requested user '+str(u.user),read=False,user=item.user_rented)
        else:
            return HttpResponse("same user cant book his car")
        return redirect('accounts:home')

@login_required
def display_req(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        cars_req=BookedCar.objects.raw("CALL Getallrequests()")
        print('used procedure')
        return render(request,'rentedcars/display_cars_req.html' ,{'cars_req':cars_req,'u':u,})


@login_required
def accept(request,req_id):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        item = BookedCar.objects.get(pk = req_id)
        if request.method == 'POST':
            for key in request.POST.items():
                if key[0] == 'decline':
                    item.delete()
        else:
            item.accept = True
            item.active = True
            item.car_rented.is_booked = True
            item.save()
            k = RentedCar.objects.get(pk=item.car_rented.pk)
            k.is_booked=True
            k.save()

            NotificationList.objects.create(message='you have succesfully accepted user '+str(item.booking_Details.user_booked.user),read=False,user=u)
            NotificationList.objects.create(message=str(u.user)+' has accepted your request',read=False,user=item.booking_Details.user_booked)
        return redirect('rentedcars:display_req')

#
# @login_required
# def decline(request,req2_id):
#     y=UserProfile.objects.get(user=request.user)
#     if y.user_type=='U':
#         item = BookedCar.objects.get(pk = req2_id)
#         item.delete()
#         return redirect('rentedcars:display_req')



@login_required
def rentalhistory(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        # SELECT * FROM rentedcars_bookedcar WHERE accept='1';
        history = BookedCar.objects.filter(accept=True)
        return render(request,'rentedcars/rentalhistory.html',{'history':history,'u':u,})








@login_required
def cab_trip(request):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        cartrip=BookedCar.objects.raw("CALL Getbookedcar()")
        # cartrip=BookedCar.objects.filter(active=True)
    return render(request,'rentedcars/cabtrip.html',{'u':u,'cartrip':cartrip,})


@login_required
def endcabtrip(request,endcab_id):
    u=UserProfile.objects.get(user=request.user)
    if u.user_type=='U':
        item = BookedCar.objects.get(pk = endcab_id)
        item.active=False
        item.save()


        rating=request.POST.get('rating')
        rented_user = UserProfile.objects.get(user=item.car_rented.user_rented.user)
        rented_user.rating=rating
        rented_user.save()
    return redirect('accounts:home')


def trial(request,trial_id):
    item = BookedCar.objects.get(pk = trial_id)
    return render(request,'rentedcars/map.html',{'item':item})

@login_required
def display_map(request,map_id):
    u=UserProfile.objects.get(user=request.user)
    trip = BookedCar.objects.get(pk = map_id)
    return render(request,'rentedcars/each_history.html',{'trip':trip})


@login_required
def car_view_history(request):
    u=UserProfile.objects.get(user=request.user)
    all_trips = BookedCar.objects.filter(active=True)
    return render(request,'rentedcars/car_history.html',{'all_trips':all_trips,'u':u})
