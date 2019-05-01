from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.models import User
from events.models import event, regUser


@login_required(login_url='/home/login/')
def index(request,eventuser):

    author = request.user.username
    print(author)

    receiver = eventuser
    print(receiver)
    room_name = "".join(sorted([author,receiver]))

    events = event.objects.all()

    mylist = []
    for item in range(len(events)):
        mylist.append(events[item].user)
    mylist = list(dict.fromkeys(mylist))

    count = 0
    print(len(mylist))
    for user in mylist:
        if(author == user.username):
            count = count+1

    all_users = User.objects.all()

    userlist = []
    if(count == 0):
        for user in range(len(all_users)):
            userlist.append(all_users[user])
        userlist = list(dict.fromkeys(userlist))

        # userlist = zip(mylist,eventlist)
    else:
        userlist = mylist

    print(userlist)

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(author)),
        'room_name': mark_safe(json.dumps(room_name)),
        'receiver': mark_safe(json.dumps(receiver)),
        'userlist': userlist,

    })
    # return render(request, 'chat/room.html',)


# @login_required(login_url='/home/login/')
# def room(request, room_name):
#     events = event.objects.all()
#     print(len(events))
#
#     mylist = []
#     for item in range(len(events)):
#         mylist.append(events[item].user)
#     mylist = list(dict.fromkeys(mylist))
#     print(mylist)
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'username': mark_safe(json.dumps(request.user.username)),
#         'userlist': mylist,
#     })