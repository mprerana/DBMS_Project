from django.contrib import admin
from .models import TVShow, Season, Episode

# Register your models here.

admin.site.register(TVShow)
admin.site.register(Season)
admin.site.register(Episode)
