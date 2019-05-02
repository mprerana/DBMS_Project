from django.urls import path, include

from django.conf.urls import include, url

from .api import *

from knox import views as knox_views

from rest_framework import routers

# Trailing edge should be added when calling api
router = routers.DefaultRouter()


router.register('api/newuserprofile',
                NewUserProfileRecordView, 'userprofile_list')


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/loggedinuser', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),

    path('api/auth/userprofile', UserProfileViewSet.as_view()),
    path('api/auth/getuserprofile/<int:pk>/', GetUserProfileViewSet.as_view()),
    path('api/auth/putuserprofile/<int:pk>/',
         UpdateUserProfileViewSet.as_view()),

    path('api/getuserregister/', RegisterUserAPI.as_view()),


    url(r'^api/auth/userprofile/update/(?P<pk>\d+)/$', UserProfileUpdate.as_view()),
    path('api/auth/user', UserListView.as_view()),
    url(r'^api/auth/user/update/(?P<pk>\d+)/$', UserView.as_view()),
    url(r'^api/newuserprofile/(?P<pk>\d+)/$', UserProfileView.as_view()),

    path('', include(router.urls))


]
