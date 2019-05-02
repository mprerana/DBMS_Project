from django.db import models

  # Create r models here.
class package(models.Model):
      user_id = models.CharField(max_length=60, null='true')
      package_id = models.CharField(max_length=60, null='true')
      origin =  models.CharField(max_length=60, null='true')
      destination = models.CharField(max_length=60, null='true')
      train = models.CharField(max_length=60, null = 'True')
      hotel = models.CharField(max_length=60, null = 'True')
      no_of_days = models.IntegerField(null = 'True')
      money = models.IntegerField(null = 'True')

def __str__(self):
     return self.package_id
