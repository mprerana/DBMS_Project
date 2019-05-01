from django import forms
from django.contrib import admin
#from .models import Complaint_Check
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.forms import TextInput
from captcha.fields import CaptchaField
from datetimepicker.widgets import DateTimePicker

"""
class Complaint_Check_Form(forms.ModelForm):
    class Meta:
        model = Complaint_Check
        fields = ['description']
"""
class test_form(forms.Form):
    captcha = CaptchaField()
