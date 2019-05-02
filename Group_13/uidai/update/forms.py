from django import forms
from captcha.fields import CaptchaField

class updateAddressForm(forms.Form):
    co = forms.CharField(label = 'C/O:')
    house = forms.CharField(label = 'House/Apt.:')
    street = forms.CharField(label = 'Street/Road:')
    landmark = forms.CharField(label = 'Landmark:')
    area = forms.CharField(label = 'Area/locality:')
    pincode = forms.IntegerField(label = 'Pincode:')
    town = forms.CharField(label = 'Village/Town/City:')
    po = forms.CharField(label = 'P.O.:')
    district = forms.CharField(label = 'District:')
    state = forms.CharField(label = 'State:')
    class Meta:
        fields = ('co','house','street','landmark','area','pincode','town','po','district','state')

class captcha(forms.Form):
    #myfield = AnyOtherField()
    captcha = CaptchaField()
