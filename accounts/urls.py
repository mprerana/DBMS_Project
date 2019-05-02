from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


app_name='accounts'


urlpatterns = [
    path('home/', views.home,name='home'),
    path('login/', views.user_login,name='user_login'),
    path('user_signup/', views.user_signup,name='user_signup'),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('taxi_profile/', views.taxi_profile,name='taxi_profile'),
    # path('driver_profile/', views.driver_profile,name='driver_profile'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('taxi_home/',views.taxi_home,name='taxi_home'),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
