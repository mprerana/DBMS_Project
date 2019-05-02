from django.urls import path
from upload_package import views

app_name = 'upload_package'

urlpatterns = [
    path('hotels/',views.UploadHotelview,name='hotels'),
    path('activity/', views.UploadActivities, name='activity'),
    path('package/', views.UploadPackview, name='package'),
    path('hostelDetails/',views.UploadDetailview,name='hostelDetails'),

]
