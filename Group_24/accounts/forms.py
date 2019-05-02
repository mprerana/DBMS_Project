from django import forms
from django.contrib.auth.models import User
from accounts.models import *
from crispy_forms.helper import FormHelper


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        password = forms.CharField(widget=forms.PasswordInput())
        model = User
        fields = ('username', 'email','password')
        widgets = {
            'username': forms.TextInput(attrs={'id':'username','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email',}),
            'password':forms.PasswordInput(attrs={'id':'password','placeholder':'Password'}),
        }

        labels = {
            'username': '',
            'email': '',
            'password': '',
            }


class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('user_type','ph_no','profile_pic',)
        widgets = {
            'ph_no': forms.TextInput(attrs={'id':'ph_no', 'placeholder':'Phone Num'}),
            'profile_pic': forms.FileInput(attrs={'id':'dp'}),
        }

        labels = {
            'ph_no': '',
            'user_type': '',
            'profile_pic': '',
            }


# class TaxiProfileForm(forms.ModelForm):
#
#     class Meta():
#         model = TaxiProfile
#         fields = ('taxi_name','taxi_num','price', )

#
# class DriverProfileForm(forms.ModelForm):
#
#     class Meta():
#         model = DriverProfile
#         fields = ('license_no','location','price' )
