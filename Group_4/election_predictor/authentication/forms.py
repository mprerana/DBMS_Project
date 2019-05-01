from django import forms
from django.contrib.auth.models import User
from authentication.models import Party, Profile


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password mismatch')
        return confirm_password


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_num', 'location', 'gender']


class PartyRegistration(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['name', 'description']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
