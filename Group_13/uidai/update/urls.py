from django.urls import path
from . import views

app_name = "update"

urlpatterns = [
    path('address/',views.update_address,name='update_address'),
    path('address/otp',views.verify_otp,name='verify_otp'),
    path('address/data_update_req',views.data_update_req,name='data_update_req'),
    path('address/data_modify',views.data_modify,name='data_modify'),
    path('address/proceed',views.proceed,name='proceed'),
    path('address/submit_document',views.submit_document,name='submit_document')
]
