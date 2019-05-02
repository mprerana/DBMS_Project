from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from User.models import Event

# class UserProfile(models.Model):
#     prof = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
#     address = models.CharField(max_length=1024,)
#     user_choice = (
#         ('V', 'Verifier'),
#         ('C', 'Customer')
#     )
#     user_type=models.CharField(choices=user_choice, max_length=2, default='C')
#
#     def __str__(self):
#         return self.prof.username

class pending_request(models.Model):
    appointed_by = models.CharField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    request_header = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    amount = models.IntegerField(validators=[MinValueValidator(50000),])
    by_date = models.DateField()
    pic = models.ImageField(upload_to='requests', default='static/userlogin/images/default-img.png')
    request_date = models.DateField()

    def __str__(self):
        return self.request_header

class pending_events(models.Model):
    appointed_by = models.CharField(max_length=255)
    event =models.ForeignKey(Event, on_delete=models.CASCADE)
