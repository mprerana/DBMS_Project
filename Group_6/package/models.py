
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import CharField
from django.db.models.fields.files import FieldFile
from django.utils import timezone
import datetime

class Amenities(models.Model):
    Amenities = models.CharField(max_length=100)

    def __str__(self):
        return self.Amenities

class Week(models.Model):
    day = models.CharField(max_length=50)
    def __str__(self):
        return self.day


class City(models.Model):
    Name = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Hotel_Address(models.Model):
    City_Id = models.ForeignKey(City, on_delete=models.CASCADE)
    Street_1 = models.CharField(max_length=100)
    Street_2 = models.CharField(max_length=100)



class Hotel(models.Model):
    Name = models.CharField(max_length=100)
    Stars = models.IntegerField()
    Type = models.CharField(max_length=100)
    Amenities = models.ManyToManyField(Amenities)
    Address = models.ForeignKey(Hotel_Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name




class Price_Hotel(models.Model):
    Hotel_Id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Per_Day = models.IntegerField()



class Key_Features(models.Model):
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key


class Trip_Package(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    Night = models.IntegerField()
    Day = models.IntegerField()
    Cost = models.IntegerField()
    Keys = models.ManyToManyField(Key_Features)
    Cities = models.ManyToManyField(City)
    Staring = models.ManyToManyField(Week)

    def __str__(self):
        return self.Title



class Trip_Origin(models.Model):
    Package_Id = models.OneToOneField(Trip_Package,on_delete=models.CASCADE)
    Origin = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.Origin


class Trip_Destination(models.Model):
    Package_Id = models.OneToOneField(Trip_Package,on_delete=models.CASCADE)
    Destination= models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.Destination

class Total_Activities(models.Model):
    City_Id = models.ForeignKey(City, on_delete=models.CASCADE)
    Activity = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    Price_Per_Person = models.IntegerField()
    Duration = models.IntegerField()
    Sutaible_For =models.CharField(max_length=255)
    Transport_Mode = models.CharField(max_length=255)

    def __str__(self):
        return self.Activity


class Package_Details(models.Model):
    Package_Id = models.ForeignKey(Trip_Package, on_delete=models.CASCADE)
    Day = models.IntegerField()
    Title = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Hotel_Id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Activities = models.ManyToManyField(Total_Activities)

    def __str__(self):
        return self.Title



class Extra_Activity(models.Model):
    Booking_Id = models.ForeignKey(Trip_Package, on_delete=models.CASCADE)
    Activity_Id = models.ForeignKey(Total_Activities, on_delete=models.CASCADE)

    def __str__(self):
        return self.Booking_Id



class Booking(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Package_Id = models.ForeignKey(Trip_Package, on_delete=models.CASCADE)
    Adults = models.IntegerField()
    Child = models.IntegerField()
    Infant = models.IntegerField()
    Date = models.DateField(default=datetime.date.today())
    Payment_Done = models.BooleanField(default=False)
    Fare = models.IntegerField(null=True)


    def __int__(self):
        return self.User_Id

class Extra_Activity(models.Model):
    Booking_Id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Activity_Id = models.ForeignKey(Total_Activities, on_delete=models.CASCADE)

    def __str__(self):
        return self.Booking_Id


class Gallery(models.Model):
    Activity_Id= models.ForeignKey(Total_Activities, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos', blank=True)


class Coustomize_package(models.Model):
    Cities = models.ManyToManyField(City)
    Days = models.IntegerField()
    Budget = models.IntegerField()
    Keys = models.ManyToManyField(Key_Features)
