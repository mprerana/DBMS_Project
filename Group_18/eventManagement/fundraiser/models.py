from django.db import models
from django.contrib.auth.models import User

from events.models import event


class eventdeet(models.Model):

    eventname=models.ForeignKey(event,on_delete=models.CASCADE, related_name='fundraiser_event')
    creator=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=1000)
    account_number = models.BigIntegerField()
    accountholder_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=10)
    funds=models.BigIntegerField(default=0)

class transactions(models.Model):
    eventname=models.CharField(max_length=1000,null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='donating_user')
    timestamp=models.IntegerField()
    paid = models.BooleanField(default=False)
    amount=models.IntegerField()
