from django import forms
from django.db import models
from shop.models import Document

class ShopAdd(forms.Form):
    sname = forms.CharField()
    a_id=forms.IntegerField()
    open_time=forms.CharField()
    close_time = forms.CharField()
    Registered_for=forms.IntegerField()
    tid=forms.IntegerField()
    owner_name=forms.CharField()
    tenant_name = forms.CharField()
    floor = forms.IntegerField()
    Description=forms.CharField()

class writereview(forms.Form):
    review = forms.CharField()
    name = forms.CharField()


