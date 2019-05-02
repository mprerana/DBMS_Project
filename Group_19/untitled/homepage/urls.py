from django.urls import path
from homepage import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name='homepage'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('password_reset/',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset_confirm/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('feedback/',views.user_feedback,name="user_feedback"),

    path('profile_view/',views.profile_view,name="profile_view"),

    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('earn_rent/(?P<value>\s+)',views.earn_rent,name="earn_rent"),
    path('sell_this/(?P<value>\s+)',views.sell_this,name="sell_this"),
    path('remove_this/(?P<value>\s+)',views.remove_this,name="remove_this"),
    path('video_chat/',views.video_chat,name="video_chat"),



]
