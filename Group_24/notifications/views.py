from django.shortcuts import render, redirect
from .models import NotificationList
from accounts.models import *

# Create your views here.
def index(request):
    u=UserProfile.objects.get(user=request.user)
    latest = NotificationList.objects.filter(user=u).last()
    all_notifications = NotificationList.objects.filter(user=u)
    all_notifications.reverse()
    rev_all = list(reversed(all_notifications))
    context = {'latest':latest,
               'rev_all':all_notifications}
    return render(request,'notifications/notify.html',context)

def update(request,notify_id):
    item = NotificationList.objects.get(pk = notify_id)
    item.read = True
    item.save()
    if item.read == True:
        item.delete()
    return redirect('notifications:index')
