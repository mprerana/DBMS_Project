from django.contrib import admin

from .models import profile,Bookmark,Follower

# Register your models her

admin.site.register(profile)
admin.site.register(Bookmark)
admin.site.register(Follower)