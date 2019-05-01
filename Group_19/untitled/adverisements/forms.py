from django import forms
from django.db import models
from .models import adv


class advform(forms.ModelForm):
    class Meta:
        model = adv
        fields = ('adv_id','expiry','tenant_id','tenant_name','floor','ad_desc','deal','image')