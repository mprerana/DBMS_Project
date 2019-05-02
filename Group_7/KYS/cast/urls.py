
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cast'
urlpatterns = [
    # path("cast/<id>/",views.Cast,name='CAST'),
    # path("director/<id>/",views.Director,name='Director'),
    # path("producer/<id>/",views.Producer,name='Producer'),
    path("cast/<id>/",views.cast_details,name='cast_details'),
    path("actor/<id>/",views.cast,name="CAST"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
