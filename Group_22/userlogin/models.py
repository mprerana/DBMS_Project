from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    city = models.CharField( max_length=100)
    country=models.CharField( max_length=100)
    pincode=models.CharField( max_length=10)



    picture=models.ImageField(upload_to='profile_image', default='static/userlogin/images/default-img.png')
    phone_number = models.CharField(max_length=10,
                                    validators=[
                                        RegexValidator(
                                            regex='^[1-9]{1}[0-9]{9}$',
                                            message='Enter a valid phone number',
                                            code='invalid_cell'
                                        ),
                                    ]
                                    )
    credits=models.IntegerField(default=0)
    reports=models.IntegerField(default=0)
    email_confirmed = models.BooleanField(default=False)
    user_choice = (
        ('V', 'Verifier'),
        ('C', 'Customer')
    )
    user_type=models.CharField(choices=user_choice, max_length=2, default='C')
    signedup_time=models.DateTimeField(auto_now_add=True)



    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
