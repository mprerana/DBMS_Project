from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AccountBalance, Statement, Pending_transactions, Pending_redeem
from django.core.mail import send_mail
from django.conf import settings
from random import *
import uuid
import string
from datetime import datetime
from twilio.rest import Client
from django.utils.crypto import get_random_string

import sys
import urllib.parse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

try:
    import httplib

except:
    import http.client as httplib


def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
@login_required(login_url='plot:user_login')
def index(request):
    # request.GET.get()
    balances = AccountBalance.objects.filter(user=request.user)
    print(balances)
    balance = {'bal': balances}
    return render(request, 'credits/index.html', context=balance)

@login_required(login_url='login')

def statement(request):
    transaction = Statement.objects.filter(user=request.user).order_by('-date')[:5]
    print(transaction)
    transaction_disp = {'trans': transaction}
    return render(request, 'credits/statement.html', context=transaction_disp)

def contact(request):
    return render(request, 'credits/contact.html')

def pending_redeem(request):
    redeem_amount = request.POST['redeem_amount']
    seed()
    code = get_random_string(length=6, allowed_chars='1234567890')
    if have_internet():
        temp = AccountBalance.objects.get(user=request.user)
        y1 = float(temp.balance) - float(redeem_amount)
        if float(redeem_amount) < 0:
            return HttpResponse('<html><script>alert("Enter valid amount");window.location="/credits";</script></html>')
        if float(temp.balance) < 200:
            return HttpResponse('<html><script>alert("Minimum balance should be 200 credits");window.location="/credits";</script></html>')
        if y1 < 0:
            return HttpResponse('<html><script>alert("Insufficient Funds");window.location="/credits";</script></html>')
        else:
            mobile_number = request.user.userprofile.phone_number
            Pending_redeem.objects.create(user=request.user, redeem_amount=redeem_amount,transaction_id="RED"+uuid.uuid4().hex[:9].upper(), code=int(code))
            auth_token = "7f7afc0c7b5a8e3b39b82d374af486a4"
            account_sid = "ACe24048a852b18d18ac49658450803864"
            try:
                client = Client(account_sid, auth_token)
                client.messages.create(
                     to="+91" + str(mobile_number),
                     from_="+18649900776",
                     body="Use {} code for verification.Amount requested to redeem is {}".format(code, redeem_amount))
            except:
                client = Client(account_sid, auth_token)
                client.messages.create(
                    to="+917842149220",
                    from_="+18649900776",
                    body="Use {} code for verification.Amount requested to redeem is {}".format(code, redeem_amount))
    else:
        return HttpResponse('<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("No internet available");window.location="/credits";</script></head></html>')
    return render(request, 'credits/pending_redeem.html')



def verify_sms(request):
    code = int(request.POST['code'])
    temp1 = Pending_redeem.objects.get(user=request.user)
    redeem_amount = temp1.redeem_amount
    temp = AccountBalance.objects.get(user=request.user)
    y1 = float(temp.balance) - float(redeem_amount)
    # temp2 = Statement.objects.get(user=1)
    # z1 = float(temp2.last1)
    # z2 = float(temp2.last2)
    # z3 = float(temp2.last3)
    # z4 = float(temp2.last4)
    # z5 = float(temp2.last5)
    key_err_page = '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("You have entered incorrect key");window.location="/credits";</script></head></html>'
    key_success_page = '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("You have redeemed successfully ");window.location="/credits";</script></head></html>'
    if code == temp1.code:
            AccountBalance.objects.filter(user=request.user).update(balance=y1)
            # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4, transaction_id_4=temp2.transaction_id_3, transaction_id_3=temp2.transaction_id_2, transaction_id_2=temp2.transaction_id_1, transaction_id_1=temp1.transaction_id, last5=z4, last4=z3, last3=z2, last2=z1, last1=redeem_amount, date5=temp2.date4, date4=temp2.date3, date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
            Statement.objects.create(user=request.user,amount=redeem_amount,transaction_id=temp1.transaction_id)
            temp1.delete()
            return HttpResponse(key_success_page)
    else:
        Statement.objects.create(user=request.user, transaction_id="FAILED")
        temp1.delete()
        return HttpResponse(key_err_page)


def random_key():
    seed()
    key = uuid.uuid4().hex[:8]
    return key

def pending_transactions(request):
    add_amount = request.POST['add_amount']
    if float(add_amount) > 0:
        key = random_key()
        if have_internet():
            user_email = request.user.email
            Pending_transactions.objects.create(user=request.user, pending_amount=add_amount, key=key)
            subject = 'Payment confirmation'
            message = ('Please use this key for confirmation {}'.format(key))
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email,]
            send_mail( subject, message, email_from, recipient_list)
            return render(request, 'credits/pending_pay.html')
        else:
            return HttpResponse('<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Internet not available");window.location="/credits";</script></head></html>')

    else:
        return HttpResponse('<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Enter a valid amount");window.location="/credits";</script></head></html>')
def pending_transactions_paypal(request):
    add_amount = request.POST['add_amount']
    if float(add_amount) > 0:
        paypal = {'paypal':add_amount}
        if have_internet():
            Pending_transactions.objects.create(user=request.user, pending_amount=add_amount, key=random_key())
        else:
            return HttpResponse('<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Internet Not available");window.location="/credits";</script></head></html>')
        return render(request, 'credits/pending_pay_paypal.html', context=paypal)
    else:
        return HttpResponse('<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Enter a valid amount");window.location="/credits";</script></head></html>')

def confirm(request):
    pay_key = request.POST['pay_key']
    temp1 = Pending_transactions.objects.get(user=request.user)
    add_amount = temp1.pending_amount
    # temp2 = Statement.objects.get(user=1)
    # z1 = float(temp2.last1)
    # z2 = float(temp2.last2)
    # z3 = float(temp2.last3)
    # z4 = float(temp2.last4)
    # z5 = float(temp2.last5)
    key_err_page = '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Key is incorrect");window.location="/credits";</script></head></html>'
    key_success_page = '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};alert("Successfully added credits");window.location="/credits";</script></head></html>'
    if pay_key == temp1.key:
        temp = AccountBalance.objects.get(user=request.user)
        y1 = float(temp.balance) + float(add_amount)
        AccountBalance.objects.filter(user=request.user).update(balance=y1)
        # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4,
        #                                           transaction_id_4=temp2.transaction_id_3,
        #                                           transaction_id_3=temp2.transaction_id_2,
        #                                           transaction_id_2=temp2.transaction_id_1,
        #                                           transaction_id_1=temp1.transaction_id, last5=z4, last4=z3, last3=z2,
        #                                           last2=z1, last1=add_amount, date5=temp2.date4, date4=temp2.date3,
        #                                           date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
        Statement.objects.create(user=request.user,amount=add_amount,transaction_id=temp1.transaction_id)
        temp1.delete()
        return HttpResponse(key_success_page)
    else:
        # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4,
        #                                           transaction_id_4=temp2.transaction_id_3,
        #                                           transaction_id_3=temp2.transaction_id_2,
        #                                           transaction_id_2=temp2.transaction_id_1,
        #                                           transaction_id_1="CANCELLED", last5=z4, last4=z3, last3=z2,
        #                                           last2=z1, last1=0, date5=temp2.date4, date4=temp2.date3,
        #                                           date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
        Statement.objects.create(user=request.user,transaction_id="FAILED")
        temp1.delete()
        return HttpResponse(key_err_page)


def transaction_cancel(request):
    temp = Pending_transactions.objects.get(user=request.user)
    # temp2 = Statement.objects.get(user=1)
    # z1 = float(temp2.last1)
    # z2 = float(temp2.last2)
    # z3 = float(temp2.last3)
    # z4 = float(temp2.last4)
    # z5 = float(temp2.last5)
    # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4,
    #                                           transaction_id_4=temp2.transaction_id_3,
    #                                           transaction_id_3=temp2.transaction_id_2,
    #                                           transaction_id_2=temp2.transaction_id_1,
    #                                           transaction_id_1="CANCELLED", last5=z4, last4=z3, last3=z2,
    #                                           last2=z1, last1=0, date5=temp2.date4, date4=temp2.date3,
    #                                           date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
    Statement.objects.create(user=request.user, transaction_id="CANCELLED")
    temp.delete()
    return redirect('/credits')


def redeem_cancel(request):
    temp = Pending_redeem.objects.get(user=request.user)
    Statement.objects.create(user=request.user,transaction_id="CANCELLED")
    temp.delete()
    return redirect('/credits')

#
# @csrf_exempt
# def ipn_listener(request):
#     VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
#     VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'
#
#     # Switch as appropriate
#     VERIFY_URL = VERIFY_URL_TEST
#
#     # CGI preamblez
#     print ('content-type: text/plain')
#     print ()
#
#     # Read and parse query string
#     param_str = sys.stdin.readline().strip()
#     params = urllib.parse.parse_qsl(param_str)
#
#     # Add '_notify-validate' parameter
#     params.append(('cmd', '_notify-validate'))
#
#     # Post back to PayPal for validation
#
#     headers = {'content-type': 'application/x-www-form-urlencoded',
#                'user-agent': 'Python-IPN-Verification-Script'}
#     r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
#     r.raise_for_status()
#
#     # Check return message and take action as needed
#     if r.text == 'VERIFIED':
#         pass
#     elif r.text == 'INVALID':
#         pass
#     else:
#         pass

def paypal_confirm(request):
    val = request.POST['value']
    temp1 = Pending_transactions.objects.get(user=request.user)
    add_amount = temp1.pending_amount
    # temp2 = Statement.objects.get(user=1)
    # z1 = float(temp2.last1)
    # z2 = float(temp2.last2)
    # z3 = float(temp2.last3)
    # z4 = float(temp2.last4)
    # z5 = float(temp2.last5)
    if val == "1":
        # p = Paypal_confirm.objects.get(user=1)
        # p.successful = 1
        # p.save()
        temp = AccountBalance.objects.get(user=request.user)
        y1 = float(temp.balance) - float(add_amount)
        AccountBalance.objects.filter(user=request.user).update(balance=y1)
        # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4,
        #                                           transaction_id_4=temp2.transaction_id_3,
        #                                           transaction_id_3=temp2.transaction_id_2,
        #                                           transaction_id_2=temp2.transaction_id_1,
        #                                           transaction_id_1=temp1.transaction_id, last5=z4, last4=z3, last3=z2,
        #                                           last2=z1, last1=add_amount, date5=temp2.date4, date4=temp2.date3,
        #                                           date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
        Statement.objects.create(user=request.user,transaction_id=temp1.transaction_id,amount=add_amount)
        temp1.delete()

    else:
        # Statement.objects.filter(user=1).update(transaction_id_5=temp2.transaction_id_4,
        #                                           transaction_id_4=temp2.transaction_id_3,
        #                                           transaction_id_3=temp2.transaction_id_2,
        #                                           transaction_id_2=temp2.transaction_id_1,
        #                                           transaction_id_1="CANCELLED", last5=z4, last4=z3, last3=z2,
        #                                           last2=z1, last1=0, date5=temp2.date4, date4=temp2.date3,
        #                                           date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
        Statement.objects.create(user=request.user,transaction_id="CANCELLED")
        temp1.delete()
    return HttpResponse(status=200)
