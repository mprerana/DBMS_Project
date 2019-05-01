from django.urls import path
from customer import views
app_name = 'customer'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout , name='user_logout'),
    path('register/', views.user_registration, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/', views.update_profile, name='profile')

]