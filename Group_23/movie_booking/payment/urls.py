from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from movie_booking import settings

urlpatterns = [

    path('1/payment/', views.pay, name='pay'),
    path('1/payment/check', views.check, name='check'),
    path('1/payment/status/', views.status, name='status'),
    path('1/payment/fineform/', views.pay_fine, name='payfine'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
