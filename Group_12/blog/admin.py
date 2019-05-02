from django.contrib import admin

from .models import Blog, Comment, interest,Deleted_Post

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(interest)
admin.site.register(Deleted_Post)