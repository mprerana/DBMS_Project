from django.shortcuts import render
from foodtruck.forms import foodcollectrequest
from foodtruck.models import Food
from django.shortcuts import render,redirect
from login.urls import *
# Create your views here.
def foodrequest(request):
    if request.method=='POST':
        foodform=foodcollectrequest(request.POST)

        if foodform.is_valid():
            name=foodform.cleaned_data.get('name')
            phone_number=foodform.cleaned_data.get('phone_number')
            address=foodform.cleaned_data.get('address')
            city=foodform.cleaned_data.get('city')
            country=foodform.cleaned_data.get('country')
            pincode=foodform.cleaned_data.get('pincode')

            data=Food.objects.create(name=name,phone_number=phone_number,pickup_address=address,city=city,country=country,pincode=pincode,user=request.user)
            data.save()
            return redirect('User:User.events')


    else:
        foodform=foodcollectrequest()
        print(foodform)
        return render(request,'foodtruck/foodcollectrequest.html',{'form':foodform})
