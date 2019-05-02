from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('signup/',views.register,name = 'register'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/login.html'),name = 'logout'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
