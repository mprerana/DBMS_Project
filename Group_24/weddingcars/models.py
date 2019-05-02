from django.db import models
from accounts.models import *
import datetime

# Create your models here.
class WeddingCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=50)
    car_photo = models.ImageField(upload_to='images/weddingcar')
    price = models.IntegerField()
    is_booked = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields = ['is_booked',]),
        ]


class BookedWeddingCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booked = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    wedding_car = models.ForeignKey(WeddingCar,on_delete=models.CASCADE)
    booked_date = models.DateField()
