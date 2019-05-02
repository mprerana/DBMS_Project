from django.db import models
from accounts.models import *
import datetime

# Create your models here.
class TouristCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    to_location = models.CharField(max_length=100)
    car_photo = models.ImageField(upload_to='images/tourists')
    price = models.IntegerField()
    no_of_days = models.IntegerField()
    is_booked = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields = ['to_location','is_booked']),
        ]


class BookedTourCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booked = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    tour_car = models.ForeignKey(TouristCar,on_delete=models.CASCADE)
    date = models.DateField()
