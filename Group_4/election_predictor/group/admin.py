from django.contrib import admin

from group.models import *

# Register your models here.
admin.site.register([Group, GroupMembers, Event, Arch_Event, EventForum])
