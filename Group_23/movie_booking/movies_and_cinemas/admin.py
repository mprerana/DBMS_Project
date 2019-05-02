from django.contrib import admin
from .models import *
admin.site.register(movie)
admin.site.register(theatre)
admin.site.register(screen)
admin.site.register(ticket_price_and_time)
admin.site.register(booking_history)
admin.site.register(update_on_database)
admin.site.register(update_on_movie)
admin.site.register(update_on_theatre)
admin.site.register(update_on_screen)
admin.site.register(update_on_ticket)
