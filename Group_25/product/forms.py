from product.models import Cuisine_item
from django import forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = Cuisine_item
        fields = ('item_name', 'item_category', 'item_image', 'item_price', 'stock_quantity', 'item_desc')
