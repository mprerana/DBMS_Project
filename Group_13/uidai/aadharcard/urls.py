from django.urls import path
from . import views

app_name = "aadharcard"

urlpatterns = [
    path('download',views.download,name='download'),
    path('aadhar-card/',views.aadhar_card,name='aadhar_card'),
    path('find-uid-eid/',views.find,name = 'find'),
    path('otp_verify/',views.otp_verify,name = 'otp_verify'),
]
