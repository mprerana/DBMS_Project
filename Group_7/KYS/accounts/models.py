from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
	# dob  = models.DateField(null=True,max_length=8)
	phone = models.CharField(null=True,blank=True,max_length=20)
	age = models.IntegerField(null=True)
	# profilePic = models.ImageField(upload_to='series_posters', blank=True)
	class Meta:
		indexes = [(models.Index(fields=['age'])),
		]
