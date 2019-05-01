from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,  PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from events.models import *
from groups.models import *
from home.forms import RegistrationForm, EditProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.views.generic import UpdateView
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from home.models import *
from django.http import Http404



# Create your views here.
def index(request):
    events = event.objects.all()
    query = request.GET.get('q')
    if query:
        events = event.objects.filter(name__icontains=query)
        print(events.query)
        if not events:
            events = event.objects.filter(venue__icontains=query)
    else:
        events = event.objects.all()

    return render(request, 'home/landing.html', {'events': events})


@login_required(login_url="/home/login")
def dashboard(request):
    events = event.objects.raw("select * from events_event")
    groups = Group.objects.filter(members=request.user)
    invites = invitation.objects.raw("select * from events_invitation where to_id = %s and status = %s",[request.user.id,0])
    group = Group.objects.raw("select * from groups_Group")

    group_invites = Group_invite.objects.raw("select * from groups_group_invite where to_id = %s and status = %s", [request.user.id,0])

    group_requests_rcvd = Group_request.objects.raw(
        "select * from groups_group_request where group_id in (select id from groups_group where creator_id = %s) and request_status=%s",[request.user.id,0])

    sent_group_requests = Group_request.objects.raw("select * from groups_group_request where request_status = %s and request_from_id = %s",[0,request.user.id])

    send_requests_group = Group.objects.raw(
        'select * from groups_group where id not in(select group_id as id from groups_group_request where request_from_id = %s union select group_id as id from groups_group_members where user_id = %s)',[request.user.id,request.user.id])

    eventrequest = eventreq.objects.raw(
        "select * from events_eventreq where event_id in (select id from events_event where user_id = %s) and status = %s",
        [request.user.id, 'False'])
    myevents = event.objects.filter(user=request.user)

    attending_ev = regUser.objects.filter(user=request.user)
    rating = user_rating.objects.get(user=request.user)
    past_events = event_archive.objects.all()
    print(attending_ev)
    return render(request, 'home/test.html',
                  {'events': events, 'invites': invites,'group_invites': group_invites,
                   'sent_group_requests': sent_group_requests,
                   'send_group_request': send_requests_group, 'group_requests_rcvd': group_requests_rcvd,
                   'eventreq': eventrequest,'groups':groups,'myevents':myevents,'attending_ev':attending_ev,'past_events':past_events,'rating':rating})


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Event Manager account.'
            message = render_to_string('home/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'home/email_confirm.html')
    else:
        form = RegistrationForm()
    return render(request, 'home/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home:index')
    else:
        logout(request)
        return redirect('home:index')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.emailconfirm.email_confirmed = True
        user.save()
        login(request, user)
        # return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect('home:dashboard')
    else:
        return HttpResponse('Activation link is invalid!')




@login_required(login_url="/home/login")
def view_profile(request, username):
    user1 = get_object_or_404(User,username=username)
    #interests = Interest_Model.objects.filter(username=user)
    event_list=[]
    editable = False
    if request.user.is_authenticated and request.user == user1:
        editable = True
    # # # interestlist=[]
    # for i in interests:
    #     interestlist.append(i.interest)
    object_list = regUser.objects.filter(user=user1)
    for item in object_list:
        event_list.append(item.event)

    args = {'user':user1, 'editable':editable, 'event':event_list}
    return render(request, 'home/profile.html', args)





@login_required(login_url="/home/login")
def edit_profile(request, username):
    user = User.objects.get(username=username)
    # inters = Interest_Model.objects.filter(username=user)
    # interest_list=[]
    # for i in inters:
    #     interest_list.append(i.interest)
    if request.user.is_authenticated and request.user == user:
        if request.method == 'POST':
            user_form = EditProfileForm(request.POST, instance=request.user)
            #profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            if user_form.is_valid():
                user_form.save()
                #profile_form.save()
                # to_delete = Interest_Model.objects.filter(username=user)
                # if to_delete.exists():
                #     to_delete.delete()
                # interest_var = request.POST.get('interests')
                # interest_var = interest_var.lower().replace(","," ")
                # interest_var = interest_var.split()
                # for var in interest_var:
                #     a = User.objects.get(username=request.user.username)
                #     Interest_Model.objects.create(username=a, interest=var)
                messages.success(request, ('Your profile was successfully updated!'))
                return redirect(reverse('home:profile', args=[request.user]))
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = EditProfileForm(instance=request.user)
            #return redirect('home:dashboard')
            #profile_form = UserProfileForm(instance=request.user.userprofile)
        args = {'user_form': user_form}
        return render(request, 'home/edit_profile.html', args)
    else:
        return redirect('home:dashboard')


@login_required(login_url="/home/login")
def settings_view(request):
    return render(request, 'home/settings.html')


@login_required(login_url="/home/login")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/home/dashboard')
        else:
            return redirect('/home/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'home/change_password.html', args)


@csrf_exempt
@login_required(login_url="/home/login")
def delete_account(request):
    confirm = request.POST.get("confirm")
    print(confirm)
    if confirm=="ok":
        print("Confirm is ok")
        u = User.objects.get(username = request.user.username)
        u.delete()
        logout(request)
    return redirect('home:index')


@login_required(login_url="/home/login")
def delete_view(request):
    return render(request, 'home/delete_confirm.html')
