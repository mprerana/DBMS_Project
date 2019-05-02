from django.contrib import admin
from .models import Show,language,GENRE,review

# Register your models here.

admin.site.register(Show)
admin.site.register(language)
admin.site.register(GENRE)
admin.site.register(review)