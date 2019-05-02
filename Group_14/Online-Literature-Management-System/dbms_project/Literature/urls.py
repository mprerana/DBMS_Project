from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
#router.register('works', WorkViewSet, basename='works')
router.register('blog', BlogViewSet)
#router.register('readinglist', ReadingListViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('works/', GetAllWorks.as_view()),
    path('blogs/<int:pk>/', GetBlogs.as_view()),
    path('works/<int:pk>/', WorkViewSet.as_view()),
    path('workdetails/<int:pk>/', WorkDetailsViewSet.as_view()),
    path('postwork/<int:pk>/',WorkPostViewSet.as_view()),
    path('workdelete/<int:pk>/', WorkDeleteViewSet.as_view()),
    path('readinglist/<int:pk>/', ReadingListViewSet.as_view()),
    path('readinglistpost/<int:pk>/', ReadingListPostViewSet.as_view()),
    path('worksinreadinglist/<int:pk>/', ReadingListWorksViewSet.as_view()),
    path('postworkinreadinglist/<int:pk>/',
         ReadingListWorksPostViewSet.as_view()),
    path('deleteworkinreadinglist/<str:pk>/',
         ReadingListWorksDeleteViewSet.as_view()),
    path('readinglistdelete/<int:pk>/', ReadingListDeleteViewSet.as_view()),
    path('getfeed/<int:pk>/', GetFeed.as_view()),
    path('bloglist/<int:pk>/', BlogListViewSet.as_view()),
    path('blogpost/<int:pk>/', BlogPostViewSet.as_view()),
    path('blogdelete/<int:pk>/', BlogDeleteViewSet.as_view())


]

# path('readinglist/<int:pk>',ReadingListViewSet.as_view())
#path('upload/<int:pk>', WorkPostViewSet.as_view())
