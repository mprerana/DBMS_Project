from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from events.models import *
from datetime import date

from django.shortcuts import render, HttpResponse
from background_task import background


@background(schedule=1)
def userActivity():
    users = User.objects.all()[1:]
    inactive = User.objects.none()
    fresh = User.objects.none()

    for user in users:
        if not regUser.objects.filter(user=user).exists():
            if not event_archive_regUser.objects.filter(user=user).exists():
                fresh |= User.objects.filter(id=user.id)
            # print("Fresh users:",fresh)
            else:
                last_attended = event_archive_regUser.objects.filter(user=user).order_by('-id')
                print("Last attended event of ", user.username, last_attended[0])
                if (date.today() - last_attended[0].event.ev_end_date).days > 90:
                    print('Here')
                    inactive |= User.objects.filter(id=user.id)
                print("Inactive users:", inactive)

        print('Scheduling')
    #
    for fuser in fresh:

        print(fuser.email)
        subject = "Welcome to EventBrite"
        to_email = fuser.email
        print(fuser)
        context = {
            'name': fuser.username,
            'content': 'Hey there! Welcome to EventBrite. Browse our catalog for some exciting events and groups.'

        }
        message = render_to_string('userActivity/index.html', context)
        msg = EmailMessage(subject, message, to=[to_email])
        msg.content_subtype = 'html'

        try:
            msg.send()
            print('Successful')
        except:
            print('Unsuccessful')

    for iuser in inactive:

        print(iuser.email)
        subject = "Welcome to EventBrite"
        to_email = iuser.email
        print(iuser)
        context = {
            'name': iuser.username,
            'content': 'Hey there! Welcome to EventBrite. Browse our catalog for some exciting events and groups.'

        }
        message = render_to_string('userActivity/inactive.html', context)
        msg = EmailMessage(subject, message, to=[to_email])
        msg.content_subtype = 'html'

        try:
            msg.send()
            print('Successful')
        except:
            print('Unsuccessful')
