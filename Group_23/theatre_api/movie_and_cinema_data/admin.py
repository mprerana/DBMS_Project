from django.contrib import admin
from .models import *
admin.site.register(movie)
admin.site.register(theatre)
admin.site.register(screen)
admin.site.register(ticket_price_and_time)
admin.site.register(booked_tickets)
admin.site.register(movie_update)
admin.site.register(changes_on_theaters)
admin.site.register(changes_on_screens)
admin.site.register(ticket_update)
