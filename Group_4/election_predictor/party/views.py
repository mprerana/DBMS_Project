from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from party.forms import PaymentsForm, VerifyPayment
from authentication.models import Party, Usertype
from party.models import PaymentDetails, SecretKey
from random import seed
import uuid
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def party(request):
    party = Party.objects.get(party__user__exact=request.user)
    return render(request, 'party/party.html', {'party': party})


def verify_payment(request, credit):
    form = VerifyPayment()
    if request.method == 'POST':
        form = VerifyPayment(request.POST)
        if form.is_valid():
            value = form.cleaned_data['key']
            party = Party.objects.get(party__user__exact=request.user)
            secret_key = SecretKey.objects.get(party=party)
            if str(value) != str(secret_key):
                error = 'The key entered is incorrect'
                return render(request, 'party/verify_purchase.html', {'form': form, 'error': error})
            else:
                party = Party.objects.get(party__user__exact=request.user)
                t_id = "ADDCREDITS" + uuid.uuid4().hex[:9].upper()
                details = PaymentDetails.objects.create(party=party, amount=credit, transaction_id=t_id)
                details.save()
                secret_key.delete()
                party.credit_amount = party.credit_amount + credit
                party.save()
                return HttpResponseRedirect(reverse('authentication:party:party'))
        else:
            print('Form is invalid')
    return render(request, 'party/verify_purchase.html', {'form': form})


@login_required
def payment_details(request):
    form = PaymentsForm()
    party = Party.objects.get(party__user__exact=request.user)
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            credits = form.cleaned_data['amount']
            seed()
            key = "ADD" + uuid.uuid4().hex[:9].upper()
            s = SecretKey.objects.create(party=party, sk=key)
            s.save()
            subject = 'Add credits to your account'
            context = {
                'key': key,
                'user': request.user,
                'credit_amount': credits
            }

            html = render_to_string('party/credit_details.html', context)
            message = render_to_string('party/credit_details.html', context)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=html)
            messages.info(request, "Thank you! Your purchase was successful!")
            return HttpResponseRedirect(reverse('authentication:party:verify_payment', args=(int(credits),)))

    return render(request, 'party/payment_details.html', {'form': form, 'credit': party.credit_amount})


def data_analysis(request):
    usertype = Usertype.objects.get(user_id=request.user.pk)
    if usertype.is_party:
        profile = Party.objects.get(party__user_id=usertype.pk)
        if request.method == 'POST':
            location = request.POST['location']
            return HttpResponseRedirect(
                reverse('authentication:party:dataanalysis:polarity_analysis_location', args=(location,)))
        return render(request, 'party/data_analysis.html', {'profile': profile})


def decrease_credits(request, amount=None):
    if amount:
        usertype = Usertype.objects.get(user_id=request.user.pk)
        if usertype.is_party:
            profile = Party.objects.get(party__user_id=usertype.pk)
            if profile.credit_amount >= amount:
                profile.credit_amount = profile.credit_amount - amount
                profile.save()
                return HttpResponseRedirect(reverse('authentication:party:data_analysis'))
            else:
                error = 'You don\'t have enough credits'
                return render(request, 'party/data_analysis.html', {'profile': profile, 'error': error})
