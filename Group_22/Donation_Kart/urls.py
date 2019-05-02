"""Donation_Kart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView)
from login import views
import userlogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('bcamp/',include('bcamp.urls')),
    path('Bloodblog/',include('Blood_blog.urls')),
    path('userlogin/', include('userlogin.urls')),
    path('signup/',userlogin.views.signup,name="userlogin.signup"),
    path('login/',views.user_login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login/home.html'),name='logout'),
    path('reset-password/', PasswordResetView.as_view(template_name='userlogin/password_reset_form.html',
                                                        email_template_name="userlogin/reset_password_email.html",
                                                        success_url="done/"), name="password_reset"),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='userlogin/password_reset_done.html'),
        name="password_reset_done"),
    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
        PasswordResetConfirmView.as_view(template_name="userlogin/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path(r'reset-password/complete/',
        PasswordResetCompleteView.as_view(template_name="userlogin/password_reset_complete.html"),
        name="password_reset_complete"),
    path('foodtruck/', include('foodtruck.urls')),
    # path('verf/', include('admin.urls')),
    path('Personal/',include('customer.urls')),
    path('User/',include('User.urls')),
    path('verf/', include('verifier.urls')),
    path('forum/', include('forum.urls')),
    path('reliffunds/', include('funds.urls')),
    path('paytm/', include('paytm.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
