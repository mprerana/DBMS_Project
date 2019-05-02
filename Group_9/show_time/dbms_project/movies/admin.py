from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Movies)
admin.site.register(Cities)
admin.site.register(City_Movie)
admin.site.register(Cast_Crew)
admin.site.register(Cast_Crew_Movie)
admin.site.register(Genre)
admin.site.register(Genre_Movie)
admin.site.register(Languages)
admin.site.register(Language_Movie)
admin.site.register(Formats)
admin.site.register(Format_Movie)
admin.site.register(Rating)
admin.site.register(Theatre_Snacks)
admin.site.register(testmodel)
admin.site.register(Booking_Ticket)
admin.site.register(Theatre_showtimings)
admin.site.register(theatre_seats)
