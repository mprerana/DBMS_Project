from django.contrib.auth.models import User
from django.db import models

from django.core.validators import RegexValidator


class UserProfile(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_choices = (
        ('U', 'user'),
        ('T', 'taxi'),
        ('D', 'driver'),
    )
    user_type=models.CharField(choices=user_choices,max_length=2,default='U')
    ph_no = models.IntegerField(null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to='images/')

    class Meta:
        indexes = [
            models.Index(fields = ['user',]),
        ]


class TaxiProfile(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    taxi_name = models.CharField(max_length=100)
    taxi_num = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields = ['location','active',]),
        ]

class DriverProfile(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    license_no = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields = ['location','is_booked','active']),
        ]
