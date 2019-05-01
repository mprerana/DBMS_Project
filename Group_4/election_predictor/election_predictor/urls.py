"""election_predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('news/', include('news_items.urls')),
    path('', views.login_user, name='login'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
            name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/reset_password.html'),
         name='forgot_pass'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_password_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_password_complete.html'),
         name='password_reset_complete'),
    re_path('api/(?P<version>(v1|v2))/', include('news_items.urls')),
    re_path('apievents/(?P<version>(v1|v2))/', include('group.urls')),

]
