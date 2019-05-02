from django import forms
from foodtruck.models  import Food
class foodcollectrequest(forms.Form):

    name=forms.CharField(min_length=1,max_length=100,required=True,widget=forms.TextInput())
    phone_number = forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    address = forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    city = forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    country = forms.CharField(min_length=1, max_length=100, required=True, widget=forms.TextInput())
    pincode = forms.CharField(min_length=1, max_length=10, required=True, widget=forms.TextInput())

    class Meta:
        model = Food
        fields = ['name', 'phone_number', 'address', 'city', 'country', 'pincode']

