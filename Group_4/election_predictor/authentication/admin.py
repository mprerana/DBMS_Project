from django.contrib import admin
from authentication.models import Profile, Party, Usertype

admin.site.register([Profile, Party, Usertype])
