from django import forms
from funds.models import funds, Images

class fund_form(forms.ModelForm):
    class Meta:
        model = funds
        exclude = ['started_on','by',]
        widgets = {
            'title':forms.TextInput(attrs={'id':'title', 'placeholder':'Title'}),
            'report':forms.Textarea(attrs={'placeholder':'Describe the incidents breifly','cols': 8, 'rows': 4, 'id':'report'}),
            'place':forms.TextInput(attrs={'id':'place', 'placeholder':'city'}),
            'state':forms.TextInput(attrs={'id':'state', 'placeholder':'state'}),
            'target':forms.NumberInput(attrs={'id':'targetamt'}),
        }
        labels = {
            'title':'',
            'report':'',
            'place':'',
            'state':'',
            'target':'',
        }

class imgform(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )
        labels = {
            'image':'',
        }
