from django.contrib import admin
from shop.models import *

admin.site.register(Product)
admin.site.register(PurchaseItem)
admin.site.register(Order)
# Register your models here.