from django.urls import path, re_path
from django.conf.urls import url

from .views import index

app_name = 'chat'

urlpatterns = [
    path('<slug:eventuser>', index, name='index'),
    # re_path(r'^(?P<eventuser>[^/]+)/$', index, name='room'),

]