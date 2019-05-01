from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(categories)
admin.site.register(event)
admin.site.register(invitation)
admin.site.register(review)
admin.site.register(eventreq)
admin.site.register(event_archive)
admin.site.register(regUser)
admin.site.register(event_archive_regUser)
