from django.urls import path
from emergencycontacts import views

app_name='emergencycontacts'

urlpatterns=[
    path('add/',views.emergencycontact,name='emergencycontacts'),
    path('sendmail',views.sendmail,name='sendmail'),
]
