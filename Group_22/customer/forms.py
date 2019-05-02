from django import forms
from customer.models import request
from datetime import date

class request_form(forms.ModelForm):

    class Meta:
        model = request

        fields = ['request_header','description' , 'amount', 'by_date', 'pic']
        widgets = {
                'by_date': forms.DateInput(attrs={'id':'date','type':'date'}),
                'description': forms.Textarea(attrs={'placeholder':'What do you need the money for ?','cols': 8, 'rows': 4, 'id':'descrip'}),
                'request_header': forms.TextInput(attrs={'id':'title', 'placeholder':'Title'}),
                'amount': forms.NumberInput(attrs={'id':'amt'}),
            }
        labels = {
                'request_header': '',
                'description': '',
                'amount': '',
                'by_date': '',
                'pic':'',
            }

def clean_by_date(self):
        date1 = self.cleaned_data['by_date']
        if date1 < date.today():
            raise forms.ValidationError("Date can't be in the past!")
        return date1
