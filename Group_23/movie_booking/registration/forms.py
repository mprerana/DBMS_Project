from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=6,max_length=100)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(min_length=6,widget=forms.PasswordInput())
    confirm_password = forms.CharField(min_length=6,widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserchangeForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=300, help_text='Required')

    class Meta():
        model = User
        fields = ('username', 'email')

    def save(self, user=None):
        user_profile = super(UserchangeForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile

class UserprofilechangeForm(forms.ModelForm):  # 1 to 1 link with Django User
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=32)

    class Meta():
        model = Profile
        fields = ('firstname','lastname','mobile')

    def save(self,user=None):
        user_profile = super(UserprofilechangeForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile