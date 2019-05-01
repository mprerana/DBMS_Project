from django import forms
from party.models import PaymentDetails
from django.forms import ValidationError


def cvv_validate(cvv):
    if len(str(cvv)) != 3:
        raise ValidationError('The CVV must have 3 digits only')
    elif int(cvv) < 0:
        raise ValidationError('The phone number must be positive')


def card_number_validate(cnum):
    if len(str(cnum)) != 16:
        raise ValidationError('The Card number must have 16 digits only')
    elif int(cnum) < 0:
        raise ValidationError('The phone number must be positive')


class VerifyPayment(forms.Form):
     key = forms.CharField(widget=forms.PasswordInput(), max_length=100)


class PaymentsForm(forms.ModelForm):
    card_number = forms.IntegerField(validators=[card_number_validate])
    card_name = forms.CharField(max_length=1000)
    cvv = forms.IntegerField(widget=forms.PasswordInput(), validators=[cvv_validate])

    class Meta:
        model = PaymentDetails
        fields = ['amount']
