from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, default=None)
    last_name = models.CharField(max_length=50, null=False, default=None)
    email = models.EmailField(max_length=200, null=False, default=None)
    cust_phone = models.CharField(max_length=10, null=False)
    cust_address = models.CharField(max_length=100, blank=True)
    cust_city = models.CharField(max_length=50, blank=True)
    cust_zipcode = models.CharField(max_length=6, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['user','cust_phone']),
        ]

    def __str__(self):
        return '%d  %s' %(self.id, self.user.username )


def create_customer(sender, **kwargs):
    if kwargs['created']:
        customer = Customer.objects.create(user=kwargs['instance'])


post_save.connect(create_customer, sender=User)


def pre_save_set_fields(sender, instance, *args, **kwargs):

    instance.first_name = instance.user.first_name
    instance.last_name = instance.user.last_name
    instance.email = instance.user.email


pre_save.connect(pre_save_set_fields, sender=Customer)

