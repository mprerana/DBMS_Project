from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User

gender_choices = (('Male', 'Male'), ('Female', 'Female'))


class Usertype(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_user = models.BooleanField(default=False)
    is_party = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Party(models.Model):
    party = models.ForeignKey(Usertype, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    credit_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.party.user.username


def phone_number_validation(ph_num):
    if len(str(ph_num)) != 10:
        raise ValidationError('The phone number must have 10 digits only')
    elif ph_num < 0:
        raise ValidationError('The phone number must be positive')


class Profile(models.Model):
    profile = models.ForeignKey(Usertype, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    phone_num = models.BigIntegerField(null=True, validators=[phone_number_validation])
    location = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=20, choices=gender_choices, null=True)
    party_id = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.profile.user.username


class Affiliation(models.Model):
    user = models.ForeignKey(Usertype, on_delete=models.CASCADE, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True)
    time = models.TimeField(auto_now_add=True)
