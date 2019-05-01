from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
from decimal import Decimal

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from fundraiser.forms import fundraiserForm
from fundraiser.models import eventdeet
from django.contrib.auth.models import User
from events.models import event




def index(request):
    fundraisers = eventdeet.objects.all()
    return render(request, 'fundraiser/index.html',{'fundraiser': fundraisers})


def startproject(request):
    user = get_object_or_404(User, username=request.user)
    eventlist=event.objects.filter(user=user)
    print(eventlist)

    if request.method == 'POST':
        form = fundraiserForm(request.POST, request.FILES)
        print('check')
        if form.is_valid():
            print('checkinggg')

            #eventname = form.cleaned_data['eventname']
            #print(eventname)
            eventname=request.POST.get('eventname')
            event1=get_object_or_404(event,name=eventname)
            description = form.cleaned_data['description']
            account_number = form.cleaned_data['account_number']
            accountholder_name = form.cleaned_data['accountholder_name']
            ifsc_code = form.cleaned_data['ifsc_code']

            temp = eventdeet.objects.create(creator=user, eventname=event1,
                                             description=description,
                                             accountholder_name=accountholder_name, account_number=account_number,
                                             ifsc_code=ifsc_code)

            return render(request, 'fundraiser/greet.html', {'form': form, 'name': user.username})

        else:
            print(form.errors)

    else:
        form = fundraiserForm()

    return render(request, 'fundraiser/startproject.html', {'form': form, 'eventlist':eventlist})

def donate(request):
    user = get_object_or_404(User, username=request.user)
    eventname=request.POST.get('eventname')
    context={'eventname':eventname,'username':user}
    return render(request,'fundraiser/fundform.html',context)


def payment_button(request):
    username=request.POST.get('username')
    host = request.get_host()
    amount=request.POST.get('amount')
    eventname=request.POST.get('eventname')
    event1=get_object_or_404(event,name=eventname)
    event2 = get_object_or_404(eventdeet, eventname=event1)
    #username=user.username



    paypal_dict = {
        "business":'vasundhara.s17@iiits.in',
        "amount": amount,
        "item_name": str(event2.id),
        #'invoice': str(event.id),
        'custom': str(username),
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

    return render(request,'fundraiser/payment.html', {"form" : form} )


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
