from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
#router.register('rating', ReviewViewSet)
#router.register('review', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/<int:pk>', RatingViewSet.as_view()),
    path('ratingpost/<int:pk>', RatingPostViewSet.as_view()),
    path('review/<int:pk>', ReviewViewSet.as_view()),
    path('reviewpost/<int:pk>', ReviewPostViewSet.as_view()),
]
