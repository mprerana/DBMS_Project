from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Blood_Groups = (
    ('A+', 'A-'),
    ('A-', 'A+'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
)

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender'),
)

States = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Goa', 'Goa'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('karnataka', 'karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Goa', 'Goa'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),

)

class Bcamp(models.Model):
    CampId=models.AutoField(primary_key=True)
    CampLocation=models.CharField(max_length=200,null=False)
    Address=models.TextField(null=False)
    CampStartTime=models.DateTimeField()
    CampStopTime=models.DateTimeField()
    campstatus=models.CharField(max_length=2,default = "a")

    def __str__(self):
       return str(self.CampId)

class Volunteer(models.Model):
    volunteer=models.ForeignKey(User, on_delete=models.CASCADE)
    CampId=models.ForeignKey(Bcamp, on_delete=models.CASCADE)

    def __str__(self):
       return str(self.volunteer)

class Bdetails(models.Model):
    # CampId=models.ForeignKey(Bcamp, on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=40)
    LastName=models.CharField(max_length=40)
    DonorAge=models.IntegerField(null=False)
    DonorMobile=models.IntegerField(primary_key=True)
    DonorLocality=models.CharField(max_length=40, null=False)
    DonorBgrp=models.TextField(max_length=5,choices=Blood_Groups, null=False, default="O+")
    Donoremail=models.EmailField()
    DonorGender=models.CharField(max_length=10,choices=Gender, null=False)

class NewVolunteer(models.Model):
    Vname = models.CharField(blank=False, max_length=100)
    Vemail = models.EmailField(unique=True)
    Vphone = models.CharField(max_length=11, blank=False)
    Vstate = models.CharField(max_length=30, choices=States, default='Andhra Pradesh')
    Vcity = models.CharField(blank=True, null=False, max_length=50)
    Vlocality = models.CharField(blank=False, max_length=400)
    Vhouse = models.CharField(blank=False, max_length=200)
    Vlandmark = models.CharField(blank=False, max_length=200)
    Vgender = models.CharField(max_length=15, choices=Gender)
    Vdate = models.DateTimeField(auto_now_add=True)
    Vblood = models.CharField(max_length=10, choices=Blood_Groups)

    def __str__(self):
       return str(self.Vphone)
