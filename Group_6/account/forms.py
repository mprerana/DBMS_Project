from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.forms import  UserChangeForm#,PasswordChangeForm
from account.models import *

from django.forms import ModelForm

class UserInfoForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'This Email address is already registered.')
        return email

class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get("query")
        password = self.cleaned_data.get("password")
        user_qs_final = User.objects.filter(
                Q(username__iexact=query)|
                Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final.count() != 1:
            raise forms.ValidationError("Invalid credentials -- user not exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
                # log auth tries
            raise forms.ValidationError("Invalid credentials -- passowrd invalid")
        if not user_obj.is_active:
            raise forms.ValidationError("Inactive user. Please verify your email address.")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    #email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user



class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class QueryForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('Name','Subject','Email','Message')
