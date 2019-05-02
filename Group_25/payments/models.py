from django.db import models
from order.models import Cust_order
from django.db.models.signals import pre_save
from payments.utils import unique_payment_id_generator
# Create your models here.

status = (('0', 'Processing'),
          ('1', 'Confirmed'),
          ('2', 'Cancelled'),)


class Cust_order_payment(models.Model):

    payment_id = models.CharField(max_length=6, blank=True)
    order_id = models.OneToOneField(Cust_order, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=40, blank=True)
    payment_date = models.DateTimeField(null=False, default=None)
    payment_status = models.CharField(choices=status, max_length=50, default=0)


def pre_save_create_payment_id(sender, instance, *args, **kwargs):
    if not instance.payment_id:
        instance.payment_id = unique_payment_id_generator(instance)


pre_save.connect(pre_save_create_payment_id, sender=Cust_order_payment)