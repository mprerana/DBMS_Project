from django.db import models
from accounts.models import *

# Create your models here.
class AirportCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=50)
    car_photo = models.ImageField(upload_to='images/airport')
    price = models.IntegerField()
    is_booked = models.BooleanField()
    from_airport = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields = ['from_airport','is_booked',]),
        ]

class BookedAirportCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booked = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    airport_car = models.ForeignKey(AirportCar,on_delete=models.CASCADE)
    date = models.DateField()
