from django.contrib import admin
from .models import Feed, Article, Query

# Register your models here.

admin.site.register(Feed)
admin.site.register(Article)
admin.site.register(Query)
