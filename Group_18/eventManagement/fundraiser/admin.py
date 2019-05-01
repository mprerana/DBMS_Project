from django.contrib import admin

# Register your models here.
from fundraiser.models import eventdeet,transactions

admin.site.register(eventdeet)
admin.site.register(transactions)
