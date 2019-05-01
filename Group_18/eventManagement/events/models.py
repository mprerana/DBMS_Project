from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from datetime import datetime
# from django.utils.timezone
import django.utils.timezone as p
from django.core.exceptions import ValidationError
# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class event(models.Model):
    categories = models.ForeignKey(categories, null=True, on_delete=models.SET_NULL, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    venue = models.CharField(max_length=500)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    private = models.BooleanField(default=False)
    start_date = models.DateField(default = p.now())
    start_time = models.TimeField()
    end_date = models.DateField(db_index=True)
    end_time = models.TimeField(null= True)
    product = models.ManyToManyField(Product, blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.end_date < self.start_date or ((self.end_date == self.start_date) and self.end_time <= self.start_time):
            raise ValidationError('Ending must be after starting')


class regUser(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " :" + self.event.name

class event_archive(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    categories = models.ForeignKey(categories, null=True, on_delete=models.SET_NULL, blank=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ev_name = models.CharField(max_length=50)
    ev_description = models.CharField(max_length=150)
    ev_venue = models.CharField(max_length=100)
    ev_city = models.CharField(max_length=20)
    ev_state = models.CharField(max_length=20)
    #ev_registered_users = models.ManyToManyField(User, related_name='ev_registered_user', null=True, blank=True)
    ev_private = models.BooleanField(default=False)
    ev_start_date = models.DateField(default=p.now())
    ev_start_time = models.TimeField()
    ev_end_date = models.DateField(db_index=True)
    ev_end_time = models.TimeField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, default=0)

    def __str__(self):
        return self.ev_name

class event_archive_regUser(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(event_archive, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " :" + self.event.ev_name

class invitation(models.Model):
    event = models.ForeignKey(event, null=True, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name='invited_user', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    msg = models.CharField(max_length=100)

    def __str__(self):
        return self.event.name+'--by--'+self.sender.username+'--to--'+self.to.username

class eventreq(models.Model):
    event = models.ForeignKey(event,on_delete=models.CASCADE)
    by = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.event.name+'--'+self.by.username

class review(models.Model):
    by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    date = models.DateTimeField(default = p.now())
    rating = models.PositiveSmallIntegerField(null=True,default=0)
    event = models.ForeignKey(event_archive, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.by.username + " :" + self.event.ev_name

