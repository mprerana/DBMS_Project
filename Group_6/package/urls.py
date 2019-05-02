from package import views
from django.urls import path
app_name= 'package'

urlpatterns = [
    path('index/', views.query_form_view, name='index'),
    # path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hotels/', views.hotels, name='hotels'),
    # path('custom_package/', views.custom_package, name='custom_package'),
    # path('custom_package1/', views.custom_package1, name='custom_package1'),
    # path('custom_package2/', views.custom_package2, name='custom_package2'),
    path('packages/', views.packages, name='packages'),
    path('custom/', views.Coustomize_view, name='custom'),
    path('details/<pk>/', views.details_trip_package, name='details_trip_package'),
    path('book/<pk>/', views.book_package1, name='book_package1'),
    path('book/final', views.book_package3, name='book_package3'),
    path('bookings', views.my_booking, name='bookings'),

]
