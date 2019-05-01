from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from group.forms import GroupRegistration, EventRegistration, Comments, Get_Location
from .models import GroupMembers, Group, Event, EventMembers, EventForum
from authentication.models import Profile, Usertype, Party
from django.db import connection
from .serializers import EventSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # <-- Here


class ListEventView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = Event.objects.all()
    serializer_class = EventSerializer


@login_required
def groups_list(request, p_id=None):
    if p_id:
        with connection.cursor() as cursor:
            cursor.execute('CALL get_group_list(%s)', [p_id])
            groups = cursor.fetchall()
        return render(request, 'group/group_list.html', {'groups': groups})
    else:
        return redirect('authentication:login_user')


@login_required
def create_group(request, p_id=None):
    if p_id:
        form = GroupRegistration()
        if request.method == 'POST':
            form = GroupRegistration(data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']

                with connection.cursor() as cursor:
                    cursor.execute('select authentication_party.id from authentication_party where party_id = %s',
                                   [p_id])
                    admin_id = cursor.fetchone()[0]
                try:
                    with connection.cursor() as cursor:
                        cursor.execute('insert into group_group(name, description, admin_id_id) values (%s,%s,%s)',
                                       [name, description, admin_id])
                except:
                    return render(request, 'group/create_group.html',
                                  {'form': form, 'error': 'This group already exists'})

                with connection.cursor() as cursor:
                    cursor.execute(
                        'select * from group_group where admin_id_id = (select id from authentication_party where party_id = %s)',
                        [p_id])
                    groups = cursor.fetchall()
                return render(request, 'group/group_list.html', {'groups': groups})
        else:
            return render(request, 'group/create_group.html', {'form': form})


@login_required
def update_group(request, g_id=None):
    if g_id:
        group = Group.objects.get(pk=g_id)
        if request.method == 'POST':
            group_details = GroupRegistration(request.POST, instance=group)
            if group_details.is_valid():
                try:
                    group.name = group_details.cleaned_data['name']
                    group.description = group_details.cleaned_data['description']
                    group.save()
                    party = Party.objects.get(pk=group.admin_id_id)
                    return HttpResponseRedirect(reverse('authentication:group:group_list', args=(party.party_id,)))
                except:
                    return render(request, 'group/edit_group.html',
                                  {'form': group_details, 'error': 'This group already exists'})
        else:
            group_details = GroupRegistration(instance=group)
            return render(request, 'group/edit_group.html', {'form': group_details})


@login_required
def event_list(request, g_id=None):
    if g_id:
        # event = Event.objects.filter(group_id_id=g_id)
        with connection.cursor() as cursor:
            cursor.execute('select * from group_event where group_id_id = %s', [g_id])
            event = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute('select * from group_group where id = %s', [g_id])
            group = cursor.fetchall()
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_party:
            return render(request, 'group/party_event_list.html',
                          {'event': event, 'group': group[0], 'usertype': usertype})
        else:
            return render(request, 'group/user_event_list.html',
                          {'event': event, 'group': group[0], 'usertype': usertype})
    else:
        return redirect('authentication:group:group_list')


@login_required
def create_event(request, g_id=None):
    if g_id:
        form = EventRegistration()
        if request.method == 'POST':
            form = EventRegistration(data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                date = form.cleaned_data['date']
                location = form.cleaned_data['location']
                # group_id = Group.objects.get(pk=g_id)
                # with connection.cursor() as cursor:
                #     cursor.execute('select group_group.id from group_group where admin_id_id = %s', [g_id])
                #     admin_id = cursor.fetchone()[0]
                # Event.objects.create(name=name, description=description,
                #                      date=date, day=day, location=location,
                #                      group_id=group_id)
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            'insert into group_event(name, description, location, date, group_id_id) values (%s, %s, %s, %s, %s)',
                            [name, description, location, date, g_id])
                except:
                    return render(request, 'group/create_event.html',
                                  {'form': form, 'error': 'This event already exists'})

                with connection.cursor() as cursor:
                    cursor.execute('select * from group_event where group_id_id = %s', [g_id])
                    event = cursor.fetchall()
                with connection.cursor() as cursor:
                    cursor.execute('select * from group_group where id = %s', [g_id])
                    group = cursor.fetchall()
                usertype = Usertype.objects.get(user_id=request.user.pk)
                if usertype.is_party:
                    return render(request, 'group/party_event_list.html',
                                  {'event': event, 'g_id': g_id, 'group': group[0], 'user': usertype})
                else:
                    return render(request, 'group/user_event_list.html',
                                  {'event': event, 'g_id': g_id, 'group': group[0], 'user': usertype})

        else:
            return render(request, 'group/create_event.html', {'form': form, })


@login_required
def update_event(request, event_id):
    if event_id:
        event = Event.objects.get(pk=event_id)
        if request.method == 'POST':
            event_details = EventRegistration(request.POST, instance=event)
            if event_details.is_valid():
                try:
                    event.name = event_details.cleaned_data['name']
                    event.description = event_details.cleaned_data['description']
                    event.location = event_details.cleaned_data['location']
                    event.date = event_details.cleaned_data['date']
                    event.save()
                    return event_list(request, event.group_id_id)
                except:
                    return render(request, 'group/edit_event.html',
                                  {'form': event_details, 'error': 'This event already exists'})

        else:
            event_details = EventRegistration(instance=event)
            return render(request, 'group/edit_event.html', {'form': event_details})


@login_required
def members_list(request, g_id=None):
    if g_id:
        group_members = GroupMembers.objects.filter(group_id_id=g_id, status=True)
        user_id = []
        for i in group_members:
            user_id.append(i.user_id_id)
        members = Profile.objects.filter(pk__in=user_id)
        user = Usertype.objects.get(user_id=request.user.pk)
        if user.is_party:
            return render(request, 'group/party_member_list.html', {'members': members, 'g_id': g_id})
        else:
            return render(request, 'group/user_member_list.html', {'members': members, 'g_id': g_id})


trig_executed = False


@login_required
def add_group_members(request, g_id=None):
    global trig_executed
    trig = '''DELIMITER //
    CREATE TRIGGER before_group_affiliation_update 
    BEFORE UPDATE ON group_groupmembers
    FOR EACH ROW 
        BEGIN
            INSERT INTO group_affiliation_archive(member_id,group_id,changedat)
            values (OLD.user_id_id,OLD.group_id_id, NOW()); 
    END //
    DELIMITER ;'''
    if not trig_executed:
        with connection.cursor() as cursor:
            # cursor.execute(trig)
            trig_executed = True
    if g_id:
        group_members = GroupMembers.objects.filter(group_id_id=g_id)
        user_id = []
        for i in group_members:
            user_id.append(i.user_id_id)
        party = Group.objects.get(pk=g_id).admin_id
        members = Profile.objects.exclude(pk__in=user_id).filter(party_id=party)
        return render(request, 'group/add_group_members.html', {'members': members, 'g_id': g_id})


@login_required
def request_member(request, g_id=None, u_id=None):
    if g_id and u_id:
        GroupMembers.objects.create(user_id_id=u_id, group_id_id=g_id)
    return HttpResponseRedirect(reverse('authentication:group:add_group_members', args=(g_id,)))


@login_required
def requested_members(request, g_id=None):
    if g_id:
        group_members = GroupMembers.objects.filter(group_id_id=g_id, status=False)
        user_id = []
        for i in group_members:
            user_id.append(i.user_id_id)
        members = Profile.objects.filter(pk__in=user_id)
        return render(request, 'group/requested_member_list.html', {'members': members, 'g_id': g_id})


@login_required
def delete_request(request, g_id=None, u_id=None):
    if g_id and u_id:
        instance = GroupMembers.objects.get(user_id_id=u_id, group_id_id=g_id)
        instance.delete()
    return HttpResponseRedirect(reverse('authentication:group:requested_members', args=(g_id,)))


@login_required
def user_groups(request, u_id=None):
    if u_id:
        u_id = Profile.objects.get(profile__user_id=u_id)
        group_members = GroupMembers.objects.filter(user_id=u_id, status=True)
        group_id = []
        for i in group_members:
            group_id.append(i.group_id_id)
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    'SELECT * FROM group_group WHERE group_group.id IN %s', [group_id])
                groups = cursor.fetchall()
        except:
            groups = ()
        return render(request, 'group/user_group_list.html', {'groups': groups, 'u_id': u_id})


@login_required
def user_requested(request, u_id=None):
    if u_id:
        u_id = Profile.objects.get(profile__user_id=u_id)
        group_members = GroupMembers.objects.filter(user_id=u_id, status=False)
        group_id = []
        for i in group_members:
            group_id.append(i.group_id_id)
        groups = Group.objects.filter(pk__in=group_id)
        return render(request, 'group/user_requested.html', {'groups': groups, 'u_id': u_id})


@login_required
def user_accept(request, g_id=None, u_id=None):
    if g_id and u_id:
        instance = GroupMembers.objects.get(user_id_id=u_id, group_id_id=g_id)
        instance.status = True
        instance.save()
    return HttpResponseRedirect(reverse('authentication:group:user_requested', args=(request.user.pk,)))


@login_required
def user_decline(request, g_id=None, u_id=None):
    if g_id and u_id:
        instance = GroupMembers.objects.get(user_id_id=u_id, group_id_id=g_id)
        instance.delete()
    return HttpResponseRedirect(reverse('authentication:group:user_requested', args=(request.user.pk,)))


@login_required
def exit_group(request, g_id=None, u_id=None):
    if g_id and u_id:
        u_id = Profile.objects.get(profile__user_id=u_id)
        instance = GroupMembers.objects.get(user_id_id=u_id.pk, group_id_id=g_id)
        instance.delete()
    return HttpResponseRedirect(reverse('authentication:group:user_groups', args=(request.user.pk,)))


@login_required
def events_location(request):
    requested = False
    get_location = Get_Location()
    usertype = Usertype.objects.get(user_id=request.user.pk)
    if usertype.is_user:
        profile = Profile.objects.get(profile__user_id=usertype.pk)
        event_members = EventMembers.objects.filter(user_id=profile.pk)
        event_id = []
        for i in event_members:
            event_id.append(i.event_id_id)
        if request.method == 'POST':
            form = Get_Location(request.POST)
            if form.is_valid():
                location = form.cleaned_data['location']
                requested = True
        else:
            location = profile.location
        events_joined = Event.objects.filter(pk__in=event_id).order_by('-date')
        events_not_joined = Event.objects.filter(location=location).exclude(pk__in=event_id).order_by('date').reverse()
        comments = EventForum.objects.all().order_by('-date')
        form = Comments()
        return render(request, 'group/events_location.html',
                      {'events_joined': events_joined, 'events_not_joined': events_not_joined, 'comments': comments,
                       'form': form, 'get_location': get_location, 'location': location, 'requested': requested})
    return HttpResponseRedirect(reverse('authentication:party:party'))


def delete_event(request, g_id=None, event_id=None):
    if event_id:
        try:
            event = Event.objects.get(pk=event_id)
            event.delete()
        except:
            pass
    if g_id:
        with connection.cursor() as cursor:
            cursor.execute('select * from group_event where group_id_id = %s', [g_id])
            event = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute('select * from group_group where id = %s', [g_id])
            group = cursor.fetchall()
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_party:
            return render(request, 'group/party_event_list.html',
                          {'event': event, 'group': group[0], 'usertype': usertype})
        else:
            return render(request, 'group/user_event_list.html',
                          {'event': event, 'group': group[0], 'usertype': usertype})


@login_required
def join_event(request, e_id):
    if e_id:
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_user:
            profile = Profile.objects.get(profile__user_id=usertype.pk)
            events = Event.objects.get(pk=e_id)
            instance = EventMembers.objects.create(user_id_id=profile.pk, event_id=events)
            instance.save()
            return HttpResponseRedirect(reverse('authentication:group:events_location'))


def leave_event(request, e_id):
    if e_id:
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_user:
            profile = Profile.objects.get(profile__user_id=usertype.pk)
            try:
                instance = EventMembers.objects.get(user_id=profile.pk, event_id=e_id)
                instance.delete()
            except:
                pass
            return HttpResponseRedirect(reverse('authentication:group:events_location'))


@login_required
def add_comment(request, e_id=None):
    if e_id:
        if request.method == 'POST':
            form = Comments(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment']
                profile = Profile.objects.get(profile__user=request.user)
                user_comment = EventForum.objects.create(user_id=profile, comment=comment, event_id_id=e_id)
                user_comment.save()
                return HttpResponseRedirect(reverse('authentication:group:events_location'))
            else:
                print('Form is invalid')
