from django.db import models
from accounts.models import UserProfile

# Create your models here.
class CarDetail(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=30)
    car_num = models.CharField(max_length=30)
    regno_expdt = models.DateField()
    mileage = models.IntegerField()
    user_choices = (
        ('N', 'nonac'),
        ('A', 'ac'),
    )
    car_type=models.CharField(choices=user_choices,max_length=2)
    car_pic = models.ImageField(upload_to='images/rentedcars/')

class RentedCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_rented = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    car_details = models.ForeignKey(CarDetail,on_delete=models.CASCADE)
    car_location = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.IntegerField()
    is_booked = models.BooleanField()

    class Meta:
        indexes = [
            models.Index(fields = ['car_location','from_date','to_date','is_booked',]),
        ]


class BookingDetail(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user_booked = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    car_location = models.CharField(max_length=100,default='')
    to_location = models.CharField(max_length=100,default='')

    class Meta:
        indexes = [
            models.Index(fields = ['user_booked',]),
        ]


class BookedCar(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    car_rented = models.ForeignKey(RentedCar,on_delete=models.CASCADE)
    booking_Details = models.ForeignKey(BookingDetail,on_delete=models.CASCADE)
    accept = models.BooleanField()
    active = models.BooleanField()
    date = models.DateField()

    class Meta:
        indexes = [
            models.Index(fields = ['accept','active',]),
        ]
