from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import get_object_or_404

from eventManagement import settings
from fundraiser.models import eventdeet,transactions
from paypal.standard.ipn.signals import valid_ipn_received
#from paypal.standard.ipn.signals import payment_was_successful, payment_was_flagged

from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender,**kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        print('payment successful')
        event = get_object_or_404(eventdeet, id=ipn.item_name)
        user = get_object_or_404(User, username=ipn.custom)
        existing=int(event.funds)
        event.funds= existing+ipn.mc_gross
        print(event.funds)
        trans=transactions(eventname=event.eventname,user=user,timestamp=123,paid=True,amount=ipn.mc_gross)
        # transactions.user=user.username
        #transactions.event=event.eventname
        # transactions.amount=ipn.mc_gross
        #transactions.paid=True
        event.save()
        trans.save()
        #transactions.save()





