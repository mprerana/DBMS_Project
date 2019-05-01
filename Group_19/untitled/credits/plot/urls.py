from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'plot'
urlpatterns = [
    path('view/<int:p_id>', views.view, name='view'),
    path('see/', views.see, name='see'),
    path('rent/', views.rent, name='rent'),
    path('buy/', views.buy, name='buy'),
    path('confirm/<int:p_id>', views.confirm, name='confirm'),
    path('final/<int:p_id>', views.final, name='final'),
    path('cancel/', views.cancel, name='cancel')
    ]