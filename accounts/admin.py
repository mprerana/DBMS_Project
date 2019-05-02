from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(UserProfile),
admin.site.register(TaxiProfile),
admin.site.register(DriverProfile),
