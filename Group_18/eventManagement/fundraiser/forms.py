import datetime
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, DateInput, Select, TextInput, NumberInput, forms,FileInput
from fundraiser.models import eventdeet


class fundraiserForm(ModelForm):
    class Meta:


        model = eventdeet
        fields = ['description','account_number','accountholder_name','ifsc_code']
        widgets = {
            #'eventname':TextInput(attrs={'type':'text'}),
            'description': TextInput(attrs={'type': 'text'}),
            'account_number': NumberInput(attrs={'type': 'int'}),
            'accountholder_name': TextInput(attrs={'type': 'text'}),
            'ifsc_code': TextInput(attrs={'type': 'text'}),
        }

        helper = FormHelper()
        helper.form_method = 'POST'

    def clean_date(self):
        date = self.cleaned_data['End_date']
        if date < datetime.date.today():
            raise forms.ValidationError("Sorry, Invalid Date!")
        return date
