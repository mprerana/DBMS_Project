from django import forms
from django.forms import ModelForm, Textarea
from .models import rate

CHOICES = (('1', 'First',), ('2', 'Second',))

class ReviewForm(ModelForm):
    class Meta:
        model = rate
        fields = [ 'rating', 'comment']
        #name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }


class filters(forms.Form):
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
