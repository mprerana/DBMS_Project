from django.shortcuts import render_to_response, render, get_object_or_404
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from fundraiser.models import eventdeet


def payment_button(request):
    user=request.POST.get('username')
    host = request.get_host()
    amount=request.POST.get('amount')
    eventname=request.POST.get('eventname')
    event = get_object_or_404(eventdeet, eventname=eventname)




    paypal_dict = {
        "business":'vasundhara.s17@iiits.in',
        "amount": amount,
        "item_name": str(event.id),
        #'invoice': str(event.id),

        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),

        #"notify_url": '127.0.0.1:8000/paypal_ipn/',
        #"return_url": '127.0.0.1:8000/payment_done/',
        #"cancel_return": '127.0.0.1:8000/payment_cancelled/',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request,'Paypal/payment.html', {"form" : form} )


@csrf_exempt
def payment_done(request):
    #rgs = {'post': request.POST,'get':request.GET}
    #return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})
    return render(request, 'home/homepage.html')


@csrf_exempt
def payment_cancelled(request):
    #rgs = {'post': request.POST,'get':request.GET}
    #return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})
    return render(request, 'home/homepage.html')
