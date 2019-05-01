from order.models import Cust_order
from django import forms


class OrderForm(forms.ModelForm):

    class Meta:
        model = Cust_order
        fields = '__all__'
