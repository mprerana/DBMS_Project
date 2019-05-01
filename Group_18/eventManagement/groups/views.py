from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GroupsForm
from django.contrib.auth.decorators import login_required
from .models import Group_invite
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import connection
from groups.models import *


# Create your views here.

@login_required(login_url="/accounts/login")
def groupview(request):
    if request.POST:
        form = GroupsForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO groups_group(name, description, creator_id) VALUES (%s,%s,%s)",
                               [form.cleaned_data['name'], form.cleaned_data['description'], request.user.id])
                gid = cursor.lastrowid
                cursor.close()
            for k in form.cleaned_data['members']:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO groups_group_members(group_id,user_id) VALUES (%s,%s)",
                                   [(str)(gid), k.id])
                    cursor.close()
            for k in form.cleaned_data['to']:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO groups_group_invite (group_id,to_id,status) VALUES( %s , %s , %s)",
                                   [(str)(gid), k, '0'])
                    cursor.close()
    else:
        form = GroupsForm()

    return render(request, 'groups/groups.html', {'form': form})


@login_required(login_url="/home/login")
def sendr(request):
    print("Inside Senderr")
    if request.method == 'POST':
        req = request.POST['req']
        receiver = Group.objects.get(id=req)

        print(receiver)
        if Group_request.objects.filter(group=receiver,request_from=request.user,request_status=2).exists():
            return render(request, "groups/request.html", {"message": 'You can not send request to this group'})


        elif Group.objects.filter(id=req, members=request.user).exists():
            print("Good one")
            return render(request, "groups/request.html", {"message": 'Already a member'})


        else:

            Group_request.objects.create(group=receiver, request_from=request.user, request_status=0)
            grp = Group.objects.get(id=req)
            return render(request, "groups/request_succ.html", {'grp': grp})


@login_required(login_url="/accounts/login")
def accept_invite(request):
    if request.method == 'POST':
        req = request.POST['req']
        invite = Group_invite.objects.get(id=req)
        grp = invite.group
        to = invite.to

        with connection.cursor() as cursor:
            cursor.execute("UPDATE groups_group_invite SET status = %s WHERE id = %s", [1, req])
            cursor.close()
    return render(request, 'events/reqaccept.html')


@login_required(login_url="/accounts/login")
def decline_invite(request):
    if request.method == 'POST':
        req = request.POST['req']
        invite = Group_invite.objects.get(id=req)
        grp = invite.group
        to = invite.to

        with connection.cursor() as cursor:
            cursor.execute("UPDATE groups_group_invite SET status = %s WHERE id = %s", [2, req])

            cursor.close()
    return render(request, "groups/invitation.html", {'user': to, 'grp': grp, 'message': 'declined'})


def grp_page(request,pk):
    grp = Group.objects.raw('select * from groups_group where id = %s',[pk])
    print(grp[0])
    admin_flg = 0
    mem_flg = 0
    req_flag = 0
    flag = 1
    dec_flg = 0
    inv_flg = 0
    req_check = Group.objects.raw(
        'select * from groups_group where id=%s and id in(select group_id as id from groups_group_request where request_from_id = %s and request_status=%s)',[pk,request.user.id,0])

    invite_check = Group.objects.raw(
        'select * from groups_group where id=%s and id in(select group_id as id from groups_group_invite where to_id = %s and status=%s)',
        [pk, request.user.id, 0])

    decline_req_check = Group.objects.raw(
        'select * from groups_group where id=%s and id in(select group_id as id from groups_group_request where request_from_id = %s and request_status=%s)',
        [pk, request.user.id, 2])

    mem_check = Group.objects.raw("select * from groups_group where id=%s and id in(select group_id as id from groups_group_members where user_id = %s)",[pk,request.user.id])

    admin_check = Group.objects.raw("select * from groups_group where id=%s and id in(select group_id as id from groups_group_members where creator_id = %s)",[pk,request.user.id])
    group_invites = Group_invite.objects.raw("select * from groups_group_invite where group_id=%s and to_id = %s and status = %s", [pk,request.user.id,0])


    if(len(admin_check)):
        admin_flg = 1
        flag = 0

    elif (len(mem_check)):
        print("Already a member")
        mem_flg = 1
        flag = 0

    elif(invite_check):
        flag=0
        print("You have an invite for this event")
        inv_flg=1


    elif(len(req_check)):
        print("Request has already been sent")
        req_flag = 1
        flag = 0

    elif (len(decline_req_check)):
        print("Request has been declined")
        dec_flg = 1
        flag = 0

    return render(request, "groups/group_page.html", {'group_invites':group_invites,'req_flg':req_flag,'admin_flg':admin_flg,'inv_flg':inv_flg,
                                                      'mem_flg':mem_flg,'dec_flg':dec_flg,'flag':flag,'grp':grp[0]})


    render(request,'groups/not_found.html')

    print("Sending")
    return render(request,"groups/group_page.html",{'flag':0,'grp':grp[0]})



@login_required(login_url="/home/login")
def accept_req(request):
    if request.method == 'POST':
        req = request.POST['req']
        sender = Group_request.objects.raw("select * from groups_group_request where id=%s",[req])[0]

        k = Group.objects.raw("select * from groups_group where id=%s and id in (select group_id from groups_group_members where user_id=%s)",[sender.group.id,sender.request_from.id])
        if (len(k)):
            print("Good one")
            return render(request, "groups/request.html", {"message": 'Already a member'})
        with connection.cursor() as cursor:
            cursor.execute("UPDATE groups_group_request SET request_status = %s WHERE id = %s", [1, req])
            cursor.close()

        grp = Group.objects.raw("select * from groups_group where id=%s",[sender.group.id])


        return render(request, "groups/request_acc.html", {'user': sender.request_from,'grp':grp,'message':'accepted'})


@login_required(login_url="/home/login")
def decline_req(request):
    if request.method == 'POST':
        req = request.POST['req']
        # sender = Group_request.objects.filter(id=req).delete()
        sender = Group_request.objects.raw("select * from groups_group_request where id=%s",[req])[0]
        name = sender.request_from
        grp = sender.group

        with connection.cursor() as cursor:
            cursor.execute("UPDATE groups_group_request SET request_status = %s WHERE id = %s",[2,req])
            cursor.close()
        try:
            return render(request, "groups/request_acc.html", {'user': name,'grp':grp,'message':'declined'})
        except:
            return render(request, "groups/request_acc.html", {'message':'Error occured'})



