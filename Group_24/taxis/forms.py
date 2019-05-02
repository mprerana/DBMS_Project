from django import forms
from taxis.models import *

class TaxiBookingForm(forms.ModelForm):

    class Meta():
        model = TaxiBooking
        fields = ('from_location','to_location')
