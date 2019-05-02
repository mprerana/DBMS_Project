from django import forms
from django.contrib.auth.models import User
from homepage.models import UserProfileInfo,feedback
from django.contrib import messages

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    re_password=forms.CharField()
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')
    def clean(self):
        all_clean_data=super().clean()
        username=all_clean_data['username']
        email=all_clean_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
class FeedbackForm(forms.ModelForm):
    class Meta():
        model=feedback
        fields=('name','rating','text')
