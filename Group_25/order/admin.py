from django.contrib import admin
from order.models import Cust_order,Cust_order_item,Cust_Cart,Cust_cart_item

# Register your models here.

admin.site.register(Cust_order_item)
admin.site.register(Cust_order)
admin.site.register(Cust_cart_item)
admin.site.register(Cust_Cart)
