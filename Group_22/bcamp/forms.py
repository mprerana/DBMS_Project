from django import forms
from .models import NewVolunteer,Bdetails,Bcamp
import datetime

class bcampForm(forms.ModelForm):
    class Meta:
        model=Bdetails
        fields='__all__'


class NewVolunteerForm(forms.ModelForm):
    class Meta:
        model=NewVolunteer
        fields='__all__'
        labels={
                'Vname':'Name',
                'Vemail':'Email',
                'Vphone':'Mobile Number',
                'Vhouse':'House',
                'Vlandmark':'Landmark',
                'Vlocality':'Locality',
                'Vcity':'City',
                'Vstate':'State',
                'Vgender':'Gender',
                'Vblood':'Blood group',
        }


class FilterForm(forms.Form):
    Location=forms.CharField(max_length=20)
    type=forms.CharField(max_length=15)

class NewCamp(forms.Form):
    Location = forms.CharField(max_length=25)
    Address = forms.CharField()
    Starttime=forms.DateField()
    Endtime=forms.DateField()
