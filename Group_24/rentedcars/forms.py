from django import forms
from rentedcars.models import *

from crispy_forms.helper import FormHelper



class CarDetailForm(forms.ModelForm):

    class Meta():
        model = CarDetail
        fields = ('car_name','car_num','regno_expdt','mileage','car_type','car_pic',)
        widgets={
            'car_name':forms.TextInput(attrs={'id':'car_name','placeholder':'carname'}),
            'car_num':forms.TextInput(attrs={'id':'car_num','placeholder':'car num'}),
            'regno_expdt':forms.DateInput(attrs={'id':'regno_expdt','placeholder':'regno_expdt'}),
            'mileage':forms.NumberInput(attrs={'id':'mileage','placeholder':'mileage'}),
            'car_pic':forms.FileInput(attrs={'id':'pic'})
        }
        labels={
            'car_name':'',
            'car_num':'',
            'regno_expdt':'',
            'mileage':'',
            'car_type':'',
            'car_pic':'',

        }


class RentedCarForm(forms.ModelForm):

    class Meta():
        model = RentedCar
        fields = ('from_date','to_date','price')
        widgets={
            'from_date':forms.TextInput(attrs={'id':'from_date','placeholder':'from_date'}),
            'to_date':forms.TextInput(attrs={'id':'to_date','placeholder':'to_date'}),
            'price':forms.TextInput(attrs={'id':'price','placeholder':'Price'}),
        }
        labels={
            'from_date':'',
            'to_date':'',
            'price':'',
        }


# class CarDetailForm(forms.ModelForm):
#
#     class Meta():
#         model = CarDetail
#         fields = ('car_name','car_num','regno_expdt','mileage','car_type','car_pic',)
#
# class RentedCarForm(forms.ModelForm):
#
#     class Meta():
#         model = RentedCar
#         fields = ('from_date','to_date','price')


class BookingDetailForm(forms.ModelForm):

    class Meta():
        model = BookingDetail
        fields = ('from_date','to_date')
        widgets={
            'from_date':forms.TextInput(attrs={'id':'from_date','placeholder':'from_date'}),
            'to_date':forms.TextInput(attrs={'id':'to_date','placeholder':'to_date'}),
        }
        labels={
            'from_date':'',
            'to_date':'',
        }
