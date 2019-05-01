from django.contrib import admin
from party.models import PaymentDetails, SecretKey

# Register your models here.

admin.site.register([PaymentDetails, SecretKey])
