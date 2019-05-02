from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import edit_profile, show_profile, login_page
from django.contrib.auth import views as auth_views
from .views import login_page,user_register,new_user_reg,log_out,login,sample_api,activate

app_name='registration'


app_name = 'registration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', show_profile, name='show_profile'),
    path('login/', login_page, name='login'),
    path('logout/', log_out, name='log_out'),
    path('register/', user_register, name='user_register'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),
    url(r'^new_user_reg/$', new_user_reg, name='new_user_reg'),
    url(r'^password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    url(r'^password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(r'^login/password/reset/$',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(r'^password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('api/login/', login, name="login"),
    path('api/sampleapi', sample_api),
]


