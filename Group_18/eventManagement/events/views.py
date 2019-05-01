from django.shortcuts import render, redirect
from .forms import EventForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import connection
from collections import namedtuple
from datetime import datetime
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar
from datetime import timedelta, date
import calendar
from background_task import background
import django.utils.timezone as p
# Create your views here.
@background(schedule=1)
def hello():
    print ("Hello World!",p.now())

# Create your views here.

class CalendarView(generic.ListView):
    model = event
    template_name = 'events/calendar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        print(d)
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        print(context['prev_month'])
        context['next_month'] = next_month(d)
        print(context['next_month'])
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


@login_required(login_url="/dashboard/login")
def eventView(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            category = categories.objects.get(name=form.cleaned_data['categories'])
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO events_event (start_date,start_time,end_date,end_time,description,city,state,private,venue,name,user_id,categories_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [form.cleaned_data['start_date'], (str)(form.cleaned_data['start_time']),
                     form.cleaned_data['end_date'], (str)(form.cleaned_data['end_time']),
                     form.cleaned_data['description'],
                     form.cleaned_data['city'], form.cleaned_data['state'], form.cleaned_data['private'],
                     form.cleaned_data['venue'], form.cleaned_data['name'], request.user.id, category.id])
                eid = cursor.lastrowid
                cursor.close()

                for k in form.cleaned_data['invite_users']:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "INSERT INTO events_invitation (event_id,sender_id,to_id,msg,status) VALUES( %s , %s , %s, %s, %s)",
                            [(str)(eid), request.user.id, k, form.cleaned_data['message'], 0])
                        cursor.close()
    else:
        form = EventForm()
    return render(request, 'events/events.html', {'form': form})


def EventDetails(request, pk):
    e = event.objects.raw("select * from events_event where id = %s", [pk])[0]
    admin_flg = 0
    mem_flg = 0
    req_flag = 0
    flag = 1
    dec_flg = 0
    inv_flg = 0
    req_check = event.objects.raw(
        'select * from events_event where id=%s and id in(select event_id as id from events_eventreq where by_id = %s and status=%s)',
        [pk, request.user.id, 0])

    invite_check = event.objects.raw(
        'select * from events_event where id=%s and id in(select event_id as id from events_invitation where to_id = %s and status=%s)',
        [pk, request.user.id, 0])

    decline_req_check = event.objects.raw(
        'select * from events_event where id=%s and id in(select event_id as id from events_eventreq where by_id = %s and status=%s)',
        [pk, request.user.id, 2])

    mem_check = event.objects.raw(
        "select * from events_event where id=%s and id in(select event_id as id from events_reguser where user_id = %s)",
        [pk, request.user.id])

    admin_check = event.objects.raw(
        "select * from events_event where id=%s and id in(select id from events_event where user_id = %s)",
        [pk, request.user.id])
    event_invites = invitation.objects.raw(
        "select * from events_invitation where event_id=%s and to_id = %s and status = %s", [pk, request.user.id, 0])

    if (len(admin_check)):
        admin_flg = 1
        flag = 0

    elif (len(mem_check)):
        print("Already a member")
        mem_flg = 1
        flag = 0

    elif (invite_check):
        flag = 0
        print("You have an invite for this event")
        inv_flg = 1

    elif (len(req_check)):
        print("Request has already been sent")
        req_flag = 1
        flag = 0

    elif (len(decline_req_check)):
        print("Request has been declined")
        dec_flg = 1
        flag = 0

    return render(request, "events/details.html",
                  {'event_invites': event_invites, 'req_flg': req_flag, 'admin_flg': admin_flg, 'inv_flg': inv_flg,
                   'mem_flg': mem_flg, 'dec_flg': dec_flg, 'flag': flag, 'e': e})


@login_required(login_url="/accounts/login")
def accept_invite(request):
    if request.method == 'POST':
        req = request.POST['req']
        invite = invitation.objects.get(id=req)
        ev = invite.event
        to = invite.to

        with connection.cursor() as cursor:
            cursor.execute("UPDATE events_invitation SET status = %s WHERE id = %s", [1, req])
            cursor.close()
    return render(request, "events/invitation.html", {'user': to, 'event': ev, 'message': 'accepted'})


@login_required(login_url="/accounts/login")
def decline_invite(request):
    if request.method == 'POST':
        req = request.POST['req']
        invite = invitation.objects.get(id=req)
        to = invite.to
        ev = invite.event
        with connection.cursor() as cursor:
            cursor.execute("delete from events_invitation WHERE id = %s", [req])

            cursor.close()
    return render(request, "events/invitation.html", {'user':to,'event':ev,'message': 'declined'})



def PastEventDetails(request, pk):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        rate = request.POST['rating']
        print("Rating:", rate)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO events_review (event_id,by_id,text,date,rating) VALUES (%s,%s,%s,%s,%s)",
                    [pk, request.user.id, form.cleaned_data['text'], p.now(), rate])
                cursor.close()

    e = event_archive.objects.raw("select * from events_event_archive where id = %s", [pk])[0]
    c = review.objects.raw("select * from events_review where event_id = %s", [pk])
    commentbyuser = review.objects.raw("select * from events_review where event_id = %s and by_id = %s",
                                       [pk, request.user.id])
    print(commentbyuser)
    flag = 0
    if len(commentbyuser) == 0:
        form = ReviewForm()
        print(len(commentbyuser))
        flag = 1
        return render(request, 'events/pasteventdetail.html', {'e': e, 'c': c, 'form': form, 'flag': flag})
    return render(request, 'events/pasteventdetail.html', {'e': e, 'c': c, 'flag': flag})


def send(request):
    if request.POST:
        id = request.POST['id']
        print('------------------------------', id)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO events_eventreq (status, by_id, event_id) VALUES (%s,%s,%s)",
                           [0, request.user.id, id])
            eid = cursor.lastrowid
            print(eid)
            cursor.close()
        return render(request, 'events/send.html')



def acceptreq(request):
    if request.POST:
        pk = request.POST["pk"]
        user = eventreq.objects.get(id=pk).by
        event = eventreq.objects.get(id=pk).event
        with connection.cursor() as cursor:
            cursor.execute("UPDATE events_eventreq SET status = %s WHERE id = %s", [1, pk])
            cursor.close()
        return render(request, 'events/reqaccept.html',{'user':user,'event':event,'message':'accepted'})

def deletereq(request):
    if request.POST:
        pk = request.POST["pk"]
        user = eventreq.objects.get(id=pk).by
        event = eventreq.objects.get(id=pk).event
        with connection.cursor() as cursor:
            cursor.execute("UPDATE events_eventreq SET status = %s WHERE id = %s", [2, pk])
            cursor.close()
        return render(request, 'events/reqaccept.html',{'user':user,'event':event,'message':'declined'})

def deleteguest(request):
    if request.POST:
        pk = request.POST["pk"]
        eventid = request.POST["eventid"]
        ev = event.objects.get(id=eventid)
        us = User.objects.get(id=pk)
        print(regUser.objects.get(event=ev, user=us))
        with connection.cursor() as cursor:
            cursor.execute("DELETE from events_reguser WHERE event_id = %s AND user_id = %s", [eventid, pk])
            cursor.close()
        return render(request, 'events/deleteguest.html')


def comment(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.by = request.user
            new_form.save()


    else:
        form = ReviewForm()
    return render(request, 'events/comment.html', {'form': form})


def pastevents(request):
    past_event = event_archive.objects.all()
    print('----------------------------\n',past_event)
    return render(request, 'events/pasteventdetail.html', {'pevent': past_event})

def add_product(request, pk):
    events = event.objects.filter(pk=pk)
    context = {
        'event' : events,
    }
    return render(request, 'events/product_form.html', context)

def product_form(request, pk):
    events = event.objects.get(pk=pk)
    print(events)
    name = request.POST.get('pname')
    desc = request.POST.get('desc')
    price = request.POST.get('price')
    image = request.POST.get('image')
    prod = Product.objects.get_or_create(name=name, description=desc, price=price, image=image)
    print(prod)
    events.product.add(prod[0])
    return redirect('events:details', pk=pk)