from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from userlogin.models import Profile
from django.contrib.auth.models import User
import sys
sys.setrecursionlimit(1000)
# Create your models here.


class Events_Supported(models.Model):
    type=models.CharField(max_length =50 , blank=False, null = False)
    subtype=models.CharField(max_length =50 , blank=False, null = False)


class Event(models.Model):
    eventid=models.AutoField(primary_key=True)
    requestedorganization=models.CharField(max_length =50 , blank=False, null = False)
    CHOICES = (('',"Select Type"),('1',"education"),('2',"NGO"),('3',"desasters"),)
    type=models.CharField(choices=CHOICES ,max_length =50, blank=False, null = False)
    SUB = (('',"Select Subtype"),('1',"stationary"),('2',"support"),)
    subtype=models.CharField(choices=SUB,max_length =50, blank=False, null = False)
    description=models.CharField(max_length =500 , blank=False, null = False)
    verifierassigned=models.CharField(max_length =10 , blank=False, null = True)
    status=models.BooleanField(default=False)
    verified=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    requesteddate=models.DateTimeField(auto_now_add=True,editable=False)
    enddate=models.DateTimeField(editable=True)
    img=models.ImageField(upload_to='images',blank=True)
    requesteditem=models.CharField(max_length =10 , blank=False, null = False)
    requestedquantity=models.PositiveIntegerField(default=0, blank=False, null = False)
    costperitem=models.PositiveIntegerField(default=0, blank=False, null = False)
    itemsremaining=models.PositiveIntegerField(default=0, blank=False, null = False)



class Donation(models.Model):
    donationid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    amount=models.PositiveIntegerField(default=0, blank=False, null = False)
    transactionid=models.CharField(max_length =50 , blank=False, null = False)
    item=models.CharField(max_length =10 , blank=False, null = False)
    Quantity=models.PositiveIntegerField(default=0, blank=False, null = False)
    description=models.CharField(max_length =200 , blank=False, null = False)

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    event=models.ForeignKey(Event, on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField(default=0, blank=False, null = False)
    amount=models.PositiveIntegerField(default=0, blank=False, null = False)

    def delete(self):

        return 0
