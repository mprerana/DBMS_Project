from django import forms
from User.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['eventid','verifierassigned','status','verified','deliverd','requesteddate','itemsremaining']
        CHOICES = (('',("Select Type")),('1',("education")),('2',("NGO")),('3',("desasters")),)
        SUB = (('',("Select Subtype")),('1',("stationary")),('2',("support")),)



        labels = {
            'requestedorganization':'',
            'type':'',
            'subtype':'',
            'description':'',
            'enddate':'',
            'img':'',
            'requesteditem':'',
            'requestedquantity':'',
            'costperitem':'',
        }
