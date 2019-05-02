from django import forms
from django.forms import ModelForm

from .models import City, Package_Details, Total_Activities, Coustomize_package,Booking


class Query_Form(forms.Form):
    #
    # choice = City.objects.all()
    # choice = list(choice) #converting it to queryset into string
    # choice2 = []
    # for x in choice:
    #     x = str(x)
    #     city_tuple_value = (x, x) #here (x,x) is like key value pair i.e (x = returned value after form submission, x = city name)
    #     choice2.append(city_tuple_value)
    #
    destination = forms.CharField(label='Destination')
    # travel_date = forms.DateField(label='Travel Date', widget=forms.SelectDateWidget)

class Booking_Form(ModelForm):
    class Meta:
        model = Booking
        fields = ['Adults', 'Child', 'Infant']


class CoustomForm(ModelForm):
    class Meta:
        model=Coustomize_package
        fields=['Cities','Days','Budget','Keys']


class Customized_Package_Form(forms.Form):
    activities = Total_Activities.objects.all()
    activities = list(activities)
    ACTIVITIES_CHOICES = []
    for x in activities:
        x =str(x)
        activities_tuple = (x, x)
        ACTIVITIES_CHOICES.append(activities_tuple)
    print(ACTIVITIES_CHOICES)
    Activities = forms.CharField(widget=forms.SelectMultiple(choices=ACTIVITIES_CHOICES))
