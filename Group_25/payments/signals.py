from django.shortcuts import get_object_or_404
from .models import Cust_order_payment
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Cust_order_payment, id=ipn.invoice)

        if order.total_cost() == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            order.save()