from django import forms
from group.models import Group, Event, EventForum


class GroupRegistration(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']


class EventRegistration(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date']


class Comments(forms.ModelForm):
    class Meta:
        model = EventForum
        fields = ['comment']


class Get_Location(forms.Form):
    location = forms.CharField(max_length=50)
