from django.urls import path
from account import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'account'


urlpatterns = [
    path('register/',views.register,name='register'),

    path('profile/edit',views.edit_profile,name='profile_update'),
    path('logout/',views.user_logout,name='logout'),
    path('logout/',views.user_logout,name='logout'),
    # path('profile/',views.user_profile,name='profile'),
    # path('forgot-pass/',views.forget_pass,name='forgot'),
    path('contact/', views.Queryview, name='contact'),

    path('activate/<uidb64>/<token>/',
        views.activate, name='activate'),


]
