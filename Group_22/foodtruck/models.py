from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

class Food(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=100)
    pickup_address =models.CharField(max_length=100)
    city=models.CharField( max_length=100)
    country=models.CharField( max_length=100)
    pincode=models.CharField( max_length=10)
    phone_number = models.CharField(max_length=10,
                                    validators=[
                                        RegexValidator(
                                            regex='^[1-9]{1}[0-9]{9}$',
                                            message='Enter a valid phone number',
                                            code='invalid_cell'
                                        ),
                                    ]
                                    )




