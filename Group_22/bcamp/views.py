from django.shortcuts import render,redirect
from .models import Bcamp,Bdetails
from django.views.generic import ListView
from bcamp.forms import bcampForm,NewVolunteerForm,FilterForm,NewCamp
from django.contrib import messages
from datetime import date

def BcampList(request):

    set=Bcamp.objects.all()
    for k in set :
        if date.today() > k.CampStopTime.date() :
            Bcamp.objects.filter( CampId = k.CampId ).update(campstatus = "a")
        elif date.today() == k.CampStopTime.date() :
            Bcamp.objects.filter( CampId = k.CampId ).update(campstatus = "b")
        elif date.today() < k.CampStopTime.date() :
            Bcamp.objects.filter( CampId = k.CampId ).update(campstatus = "c")

    Loc=" "
    Type="all"
    if request.method== 'POST' :
        Fform=FilterForm(request.POST)
        if Fform.is_valid():
            Loc=Fform.cleaned_data['Location']
            Type=Fform.cleaned_data['type']

    else :
        Fform=FilterForm()

    posts = Bcamp.objects.all()
    if Type=='past' :
        print("above posts")
        posts = Bcamp.objects.filter( campstatus = "a", CampLocation = Loc )
        print("below post")
        print(posts)
    elif Type=='ongoing' :
        posts = Bcamp.objects.filter( campstatus = "b" , CampLocation = Loc )
    elif Type=='upcoming' :
        posts = Bcamp.objects.filter( campstatus =  "c" , CampLocation = Loc )

    context ={ "camp" : posts, "Location" : Loc, "Type" : Type, "filter" : FilterForm }
    return render (request,"bcamp/campblog.html",context)


def CampFormView(request):
    if request.method == 'POST':
        form = bcampForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'Registration successful')
            return redirect('bcamp:BcampHome')

    else:
        form=bcampForm()

    return render(request,'bcamp/Campform.html',{'form': bcampForm })

def NewVolForm(request):
    if request.method == "POST":
        Vform = NewVolunteerForm(request.POST)

        if Vform.is_valid():
            Vform.save(commit=True)
            return redirect('bcamp:BcampHome')
    else:
        Vform=NewVolunteerForm()
        return render(request,'bcamp/NewVForm.html',{'Vform':NewVolunteerForm})


def NewCampForm(request):
    if request.method == "POST" :
        Bform=NewCamp(request.POST)

        if Bform.is_valid():
            Lo=Bform.cleaned_data['Location']
            Add=Bform.cleaned_data['Location']
            Sta=Bform.cleaned_data['Location']
            Sto=Bform.cleaned_data['Location']

            data = Bcamp(
                        CampLocation = Lo,
                        Address = Add,
                        CampStartTime = Sta,
                        CampStopTime = Sto
            )
            data.save()
            return redirect('bcamp:BcampHome')
    else :
        Bform = NewCamp()
        return render(request,'bcamp/NewCamp.html',{'Bform':NewCamp} )
