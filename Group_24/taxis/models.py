from django.db import models
from accounts.models import *
import datetime

# Create your models here.
class TaxiBooking(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booking = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        indexes = [
            models.Index(fields = ['user_booking',]),
        ]


class BookedTaxi(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    taxi_booking_details = models.ForeignKey(TaxiBooking,on_delete=models.CASCADE)
    taxi_booked = models.ForeignKey(TaxiProfile,on_delete=models.CASCADE)
    time = models.TimeField()
    active = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields = ['active',]),
            models.Index(fields = ['taxi_booking_details',]),
            models.Index(fields = ['taxi_booked',]),
        ]


class BookedDriver(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booked = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile,on_delete=models.CASCADE)
    date = models.DateField()
