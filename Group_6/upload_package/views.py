from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,reverse
from upload_package.forms import *
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from package.models import *
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory

# @login_required(login_url='login')
def UploadHotelview(request):
    if request.method=='POST':
        upload = HotelForm(data=request.POST)
        address = HotelAddForm(data=request.POST)
        price = HotelPriceForm(data=request.POST)

        if upload.is_valid() and address.is_valid() :
            form = upload.save(commit=False)
            add = address.save()
            form.Address = add
            request.session['Hotel'] = form.id
            hotel_instance=upload.save()
            print(hotel_instance)
            for amenity in hotel_instance.Amenities.all():
                hotel_instance.Amenities.add(amenity)
                hotel_instance.save()
            price_inst = price.save(commit=False)
            price_inst.Hotel_Id = form
            price.save()
            return HttpResponse('done')
        else:
            print(upload.errors,address.errors)
    else:

        hotel = HotelForm()
        address = HotelAddForm()
        price= HotelPriceForm()

    # return render(request,'hostupload/main-upload.html',{'upload':upload,'address':address})
        return render(request,'hotelupload.html',{'upload':hotel,'address':address,'price':price})


def UploadActivities(request):
    ImageFormset = modelformset_factory(Gallery, fields=('img',), extra=3 , max_num=8)

    if request.method=='POST':
        activity = ActivityForm(data=request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)

        if activity.is_valid() and formset.is_valid():
            activity_ins=activity.save()
            for file in formset:
                if file.cleaned_data:
                    try:
                        photo = Gallery(Activity_Id=activity_ins, img=file.cleaned_data.get('img'))
                        photo.save()
                    except Exception as e:
                        break
            return HttpResponse('done')

        else:
            print(activity.errors)
    else:

        upload = ActivityForm()
        ImageFormset = ImageFormset(queryset=Gallery.objects.none())



    # return render(request,'hostupload/main-upload.html',{'upload':upload,'address':address})
        return render(request,'uploadactivity.html',{'upload':upload,'image':ImageFormset})





# @login_required(login_url='login')
def UploadPackview(request):

    if request.method=='POST':
        upload = TripPackForm(data=request.POST)
        origin = TripOriginForm(data=request.POST)
        dest = TripDestForm(data=request.POST)
        if upload.is_valid() and origin.is_valid() :
            form = upload.save(commit=False)
            pack_instance=upload.save()
            orig = origin.save(commit=False)
            destin = dest.save(commit=False)
            for city in pack_instance.Cities.all():
                pack_instance.Cities.add(city)
                pack_instance.save()

            for key in pack_instance.Keys.all():
                pack_instance.Keys.add(key)
                pack_instance.save()

            orig.Package_Id = form
            destin.Package_Id = form
            destin.save()
            orig.save()

            request.session['package'] = form.id
            request.session['days'] = form.Day

            return redirect('upload_package:hostelDetails')

        else:
            print(upload.errors,address.errors)
    else:

        upload = TripPackForm()
        origin = TripOriginForm()
        dest = TripDestForm()
    # return render(request,'hostupload/main-upload.html',{'upload':upload,'address':address})
    return render(request,'uploadpackage.html',{'upload':upload,'origin':origin,'dest':dest})



def UploadDetailview(request):
    if request.method=='POST':
        pid =  request.session.get('package')
        package = Trip_Package.objects.get(pk=pid)
        form = PackageDetailForm(data=request.POST)
        if form.is_valid():
            forminst = form.save(commit=False)
            forminst.Package_Id = package
            forminst = form.save()
            for activity in forminst.Activities.all():
                forminst.Activities.add(activity)
                forminst.save()
        day = request.session.get('days')
        for i in range(day - 1):
            request.session['days'] = day-1
            return redirect('upload_package:hostelDetails')



        else:
            print(form.errors)
            
        return HttpResponse('done')

        return render(request,'packagedone.html')


    else:
        form = PackageDetailForm()
    return render(request,'packagedetails.html',{'form':form})
