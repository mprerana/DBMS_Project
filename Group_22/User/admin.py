from django.contrib import admin
from .models import Event,Donation,Events_Supported,Cart
# Register your models here.

admin.site.register(Event)
admin.site.register(Donation)
admin.site.register(Events_Supported)
admin.site.register(Cart)
