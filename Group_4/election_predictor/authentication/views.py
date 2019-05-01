from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from authentication.forms import Registration, PartyRegistration, CreateProfile, UpdateProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from authentication.models import Profile, Party
from authentication.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.db import connection


# trig_executed = False

@login_required
def list_parties(request):
    user = request.user
    user_profile = Profile.objects.get(profile__user__username=user)
    p_id = user_profile.party_id_id
    if p_id:
        parties = Party.objects.exclude(pk=p_id)
    else:
        parties = Party.objects.all()
    return render(request, 'authentication/assign_party.html', {'parties': parties})


def choose_party(request, p_id=None):
    # global trig_executed
    trig = '''DELIMITER //
    CREATE TRIGGER before_party_affiliation_update 
        BEFORE UPDATE ON authentication_profile
        FOR EACH ROW 
        BEGIN
            IF OLD.party_id_id != NEW.party_id_id THEN
                INSERT INTO authentication_affiliation(user_id,party_id,time) values(OLD.profile_id,OLD.party_id_id,NOW());
                DELETE FROM group_groupmembers WHERE user_id_id = OLD.id;
            END IF; 
            
        END //
DELIMITER ;'''
    # if not False:
    #     with connection.cursor() as cursor:
    # cursor.execute(trig)
    # trig_executed = True
    if p_id:
        user = request.user
        user_profile = Profile.objects.get(profile__user__username=user)
        user_profile.party_id_id = p_id
        user_profile.save()
        return redirect('news_items:articles_list')


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            u = User.objects.get(username=user)
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            if u.usertype.is_user:
                return redirect('news_items:articles_list')
            elif u.usertype.is_party:
                return redirect('authentication:party:party')
            else:
                return HttpResponse('User does not exist')

    return render(request, 'authentication/login.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user
    if user.usertype.is_party:
        party = Party.objects.get(party__user__username=user)
        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=user)
            form_party_details = PartyRegistration(request.POST, instance=party)
            if form.is_valid() and form_party_details.is_valid():
                user = form.save(commit=False)
                user.save()
                party.name = form_party_details.cleaned_data['name']
                party.description = form_party_details.cleaned_data['description']
                party.save()
                return redirect('authentication:party:party')

        else:
            form = UpdateProfile(instance=user)
            form_party_details = PartyRegistration(instance=party)
            return render(request, 'party/update_profile.html', {'form': form, 'form_party': form_party_details})

    elif user.usertype.is_user:
        profile = Profile.objects.get(profile__user__username=user)
        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=user)
            user_details = CreateProfile(request.POST, instance=profile)
            if form.is_valid() and user_details.is_valid():
                user = form.save(commit=False)
                user.save()
                profile.first_name = user_details.cleaned_data['first_name']
                profile.last_name = user_details.cleaned_data['last_name']
                profile.location = user_details.cleaned_data['location']
                profile.phone_num = user_details.cleaned_data['phone_num']
                profile.gender = user_details.cleaned_data['gender']

                profile.save()
                return redirect('news_items:articles_list')

        else:
            form = UpdateProfile(instance=user)
            user_details = CreateProfile(instance=profile)
            return render(request, 'party/update_profile.html', {'form': form, 'user_form': user_details})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('authentication:login_user')
    else:
        return HttpResponse('Activation link is invalid!')


def register_user(request):
    form = Registration()
    form_profile = CreateProfile()
    if request.method == 'POST':
        form = Registration(request.POST)
        form_profile = CreateProfile(request.POST)
        if form.is_valid() and form_profile.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            # ut = Usertype.objects.create(user=user, is_user=True)
            # ut.save()
            with connection.cursor() as cursor:
                cursor.execute('insert into authentication_usertype(user_id, is_user, is_party) values (%s,%s,%s)',
                               [user.pk, True, False])

            # profile = form_profile.save(commit=False)
            # profile.profile = ut
            # profile.save()
            first_name = form_profile.cleaned_data['first_name']
            last_name = form_profile.cleaned_data['last_name']
            phone_num = form_profile.cleaned_data['phone_num']
            location = form_profile.cleaned_data['location']
            gender = form_profile.cleaned_data['gender']
            with connection.cursor() as cursor:
                cursor.execute(
                    'insert into authentication_profile(first_name, last_name, phone_num, location, gender, profile_id) values (%s,%s,%s, %s,%s,%s)',
                    [first_name, last_name, phone_num, location, gender, user.pk])

            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('authentication/activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'authentication/register.html', {'form': form, 'form_profile': form_profile})


def register_party(request):
    form_basic = Registration()
    form_party = PartyRegistration()
    if request.method == 'POST':
        form_basic = Registration(request.POST)
        form_party = PartyRegistration(request.POST)
        if form_basic.is_valid() and form_party.is_valid():
            user = form_basic.save(commit=False)
            description = form_party.cleaned_data['description']
            name = form_party.cleaned_data['name']
            user.set_password(form_basic.cleaned_data['password'])
            user.save()

            # ut = Usertype.objects.create(user=user, is_party=True)
            # ut.save()
            with connection.cursor() as cursor:
                cursor.execute('insert into authentication_usertype(user_id, is_user, is_party) values (%s,%s,%s)',
                               [user.pk, False, True])
            # party = Party.objects.create(party=ut, description=description, name=name)
            # party.save()
            with connection.cursor() as cursor:
                cursor.execute(
                    'insert into authentication_party(name, description, created_at, credit_amount,party_id) values (%s,%s,%s,%s,%s)',
                    [name, description, datetime.now(), 0, user.pk])

            return redirect('authentication:login_user')

    return render(request, 'authentication/register.html',
                  {'form': form_basic, 'form_party': form_party})
