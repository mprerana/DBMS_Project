from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('appuser', AllUSERViewSet, basename='appuser')
router.register('follower', FOLLOWViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', USERViewSet.as_view()),
    path('userput/<int:pk>/', USERPutViewSet.as_view()),
    path('followers/<int:pk>/', GetFollowersViewSet.as_view()),
    path('following/<int:pk>/', GetFollowingViewSet.as_view()),
    path('follow/<str:pk>/', FollowViewSet.as_view()),
    path('unfollow/<str:pk>/', UnFollowViewSet.as_view())
]
