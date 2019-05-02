from package.models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, ButtonHolder, Submit, Div, HTML


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['Name','Stars','Type','Amenities']

    #
    # helper = FormHelper()
    # helper.layout = Layout(
    #     Field('street', css_class='form-control input_heads'),
    #     Field('city', css_class='form-control input_heads'),
    #     Field('state', css_class='form-control input_heads'),
    #     Field('zipcode', css_class='form-control input_heads'),
    #
    # )

class HotelAddForm(ModelForm):
    class Meta:
        model = Hotel_Address
        fields = ['Street_1','Street_2','City_Id']

class HotelPriceForm(ModelForm):
    class Meta:
        model = Price_Hotel
        fields = ['Per_Day']


class ActivityForm(ModelForm):
    class Meta:
        model = Total_Activities
        fields = '__all__'


class TripPackForm(ModelForm):
    class Meta:
        model = Trip_Package
        fields = ['Title','Description','Night','Day','Cost','Keys','Cities']

class TripOriginForm(ModelForm):
    class Meta:
        model = Trip_Origin
        fields = ['Origin']




class TripDestForm(ModelForm):
    class Meta:
        model = Trip_Destination
        fields = ['Destination']

class PackageDetailForm(ModelForm):
    class Meta:
        model = Package_Details
        fields = ['Day','Title','Description','City','Hotel_Id','Activities']
