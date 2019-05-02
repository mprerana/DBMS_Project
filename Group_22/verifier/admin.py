from django.contrib import admin
from verifier.models import pending_request,pending_events
# Register your models here.
admin.site.register(pending_request)
admin.site.register(pending_events)
