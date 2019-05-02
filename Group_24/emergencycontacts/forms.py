from django import forms
from django.contrib.auth.models import User
from emergencycontacts.models import *

class Emergenycontactform(forms.ModelForm):

    class Meta():
        model = EmergencyContacts
        fields=('name','contact_no','email')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'car_name', 'placeholder': 'carname'}),
            'contact_no': forms.NumberInput(attrs={'id': 'car_num', 'placeholder': 'car num'}),
            'email': forms.EmailInput(attrs={'id': 'regno_expdt', 'placeholder': 'regno_expdt'}),
            }
        labels = {
            'name': '',
            'contact_no': '',
            'email': '',
                }
