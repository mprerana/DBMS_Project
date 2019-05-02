from django.db import models
from accounts.models import *

# Create your models here.
class EmergencyContacts(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    contact_no = models.IntegerField()
    email = models.EmailField(max_length=100)
