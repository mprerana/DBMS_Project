from django.contrib import admin
from .models import peer, fileorfolder, chunkshashdb
# Register your models here.

admin.site.register(fileorfolder)
admin.site.register(peer)
admin.site.register(chunkshashdb)
