from . import views
from django.conf.urls import include,url

app_name = 'print'

urlpatterns = [
    url('',views.home, name='home'),
]
