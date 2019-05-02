from django.contrib import admin
from taxis.models import *

# Register your models here.
admin.site.register(TaxiBooking),
admin.site.register(BookedTaxi),
admin.site.register(BookedDriver),
