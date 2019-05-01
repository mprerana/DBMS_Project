from django.urls import path
from . import views

app_name = 'userActivity'

urlpatterns = [
    # path('',views.listEvent,name='list-event'),
    path('', views.userActivity, name='checkactivity'),
]
