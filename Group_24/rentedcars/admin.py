from django.contrib import admin
from rentedcars.models import *

# Register your models here.
admin.site.register(CarDetail),
admin.site.register(RentedCar),
admin.site.register(BookingDetail),
admin.site.register(BookedCar),
