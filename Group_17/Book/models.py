from django.db import models
from django.contrib.auth.models import User

class Flights(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE ,null=True,unique=False )
    flight_name=models.CharField(max_length=10,blank=True)
    flight_code=models.CharField(max_length=10,blank=True)
    date=models.DateField(blank=True,null=True)
    dept_city=models.CharField(max_length=10,blank=True)
    dept_time=models.TimeField()
    no_of_stops=models.CharField(max_length=10,blank=True)
    reach_time=models.TimeField()
    duration=models.CharField(max_length=100)
    arrival_city=models.CharField(max_length=10)
    price=models.CharField(max_length=10)
    book_date=models.DateTimeField(blank=True,null=True)
    details=models.CharField(max_length=100)


    def __str__(self):
        return self.user_id.username


class Hotels(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=False)
    hotel_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=500,blank=True)
    price = models.CharField(max_length=10)
    check_in_date = models.DateField(blank=True,null=True)
    check_out_date = models.DateField(blank=True,null=True)
    booking_date=models.DateTimeField(blank=True,null=True)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.user_id.username