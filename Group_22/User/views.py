from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Event,Events_Supported,Cart,Donation
from userlogin.models import Profile
from django.contrib.auth.decorators import login_required
from django.db import transaction,connection
from User.forms import EventForm
from funds.models import funds, Images


@login_required(login_url='login')
def home(request):
    return render(request,'User/home.html')

@login_required
def Raiserequest(request):
    print('a')
    eventform=EventForm()
    if request.method=='POST':
        eventform=EventForm(request.POST)
        if eventform.is_valid():
            print('x')
            requestedorganization=eventform.cleaned_data.get['requestedorganization']
            type=eventform.cleaned_data.get['type']
            subtype=eventform.cleaned_data.get['subtype']
            description=eventform.cleaned_data.get['description']
            enddate=eventform.cleaned_data.get['enddate']
            image=eventform.cleaned_data.get['img']
            requesteditem=eventform.cleaned_data.get['requesteditem']
            requestedquantity=eventform.cleaned_data.get['requestedquantity']
            costperitem=eventform.cleaned_data.get['costperitem']
            eventdata=Event.objects.create(requestedorganization=requestedorganization,type=type,subtype=subtype,description=description,enddate=enddate,image=image,requesteditem=requesteditem,requestedquantity=requestedquantity,costperitem=costperitem)
            eventdata.save()
            return redirect('User:home')
        else:
            print('y')
            eventform=EventForm(request.POST)
            return render(request,'User/riserequest.html',{'eventform':eventform})
    else:
        print('z')
        return render(request,'User/riserequest.html',{'eventform':eventform})

@login_required(login_url='login')
def events(request):
    eventslist=Events_Supported.objects.all()
    eventsset=[]
    for e in eventslist:
        eventsset.append(e.type)
    #eventslist=list(set(eventsset))
    cursor=connection.cursor()
    cursor.callproc('eventfilter',["all",])
    events_eme = (cursor.fetchall())
    # Event.objects.filter(completed=False).filter(verified=True).order_by('enddate')
    events_eme_list=[]
    for e in events_eme:
        temp=Event.objects.filter(eventid=e[0])
        dlist=[]
        for t in temp:
            dlist.append(t)
        donated_quantity=0
        for d in Donation.objects.filter(event_id=e[0]):
            donated_quantity+=d.Quantity
        dlist.append(donated_quantity)
        dlist.append(e[13])
        dlist.append(100-int(e[15])*100/e[14])
        dlist.append(e[14]-donated_quantity)
        dlist.append((e[14]-donated_quantity))
        events_eme_list.append(tuple(dlist))
    events_eme_list[:12]
    return render(request,'User/event2.html',context={'eventslist':eventslist,'events':events_eme_list,})


def natdis(request):
    relif = funds.objects.all()
    imgs = funds.objects.all()
    return render(request,'User/natdis.html',context={'events':relif,'imgs':imgs})


@login_required(login_url='login')
def cart(request):
    user=request.user
    if(request.POST):
        eventID=int(request.POST['eventid'])
        quantity=int(request.POST['quantity'])
        event=0
        for e in Event.objects.filter(eventid=eventID):
            event=e
        cartlist=Cart.objects.filter(user=user)
        flag=0
        for c in cartlist:
            if c.event==event:
                #quantity+=c.Quantity
                #amount=200
                #Cart.objects.filter(user=user).filter(event=event).update(Quantity=quantity)
                #Cart.objects.filter(user=user).filter(event=event).update(amount=amount)
                flag=1
        if flag==0:
            amount=quantity*event.costperitem
            Cart.objects.create(event=event,user=request.user,Quantity=quantity,amount=amount)
    cartcost=0
    cartlist=list()
    for c in Cart.objects.filter(user=user):
        for e in Event.objects.filter(verified=True):
            if c.event==e:
                cartlist.append([c,e])
                cartcost+=c.Quantity*e.costperitem
    #print(cartlist)
    count=len(cartlist)

    return render(request,'User/cart.html',context={'cartlist':cartlist,'count':count,'cartcost':cartcost})

@login_required(login_url='login')
def delete(request,id):
    event=0
    for e in Event.objects.filter(eventid=id):
        event=e
    cartItems = Cart.objects.filter(user=request.user,event=event)
    cartItems.delete()
    return cart(request)

@login_required(login_url='login')
def filter(request,id):
    eventslist=Events_Supported.objects.all()
    eventsset=[]
    for e in eventslist:
        eventsset.append(e.type)

    type=id
    print(type)
    cursor=connection.cursor()
    cursor.callproc('eventfilter',[type,])
    events_eme = (cursor.fetchall())
    # Event.objects.filter(completed=False).filter(verified=True).order_by('enddate')
    events_eme_list=[]
    for e in events_eme:
        temp=Event.objects.filter(eventid=e[0])
        dlist=[]
        for t in temp:
            dlist.append(t)
        donated_quantity=0
        for d in Donation.objects.filter(event_id=e[0]):
            donated_quantity+=d.Quantity
        dlist.append(donated_quantity)
        dlist.append(e[13])
        dlist.append(100-int(e[15])*100/e[14])
        dlist.append(e[14]-donated_quantity)
        events_eme_list.append(tuple(dlist))
    events_eme_list[:12]
    return events(request)

@login_required(login_url='login')
def proceed(request):
    user=request.user
    count=Cart.objects.filter(user=user).count()
    if count and payment(request):
        for c in Cart.objects.filter(user=user):
            for e in Event.objects.filter(verified=True):
                if c.event==e:
                    itemsremaining=e.itemsremaining-c.Quantity
                    Event.objects.filter(eventid=e.eventid).update(itemsremaining=itemsremaining)
                    Cart.objects.filter(user=user).delete()
                    return redirect('http://127.0.0.1:8000/paytm/payment/')
    return home(request)


def payment(request):
    return True
