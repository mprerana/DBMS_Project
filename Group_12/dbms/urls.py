from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from blog import views
from .views import home

from registration import views as views2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/create_blog/',views.createView.as_view()),
    url(r'^api/register/',views2.SignUpView.as_view()),
    url(r'^api/signin/', views2.SignInView.as_view()),
    url(r'^api/Blog/(?P<interest_name>[a-z A-z 0-9]+)$', views.BlogView2.as_view()),
    url(r'^api/Blog_id/(?P<blog_id>[0-9]+)$', views.BlogbyIdView2.as_view()),
    url(r'^api/interests/', views.interestView.as_view()),
    url(r'^api/profileposts/', views.profilepostView.as_view()),
    url(r'^api/likebutton/', views.likebutton.as_view()),
    url(r'^api/Bookmark/', views.BookmarkView.as_view()),
    url(r'^api/followview/', views.followview.as_view()),
    url(r'^api/followers1/(?P<user_id>[a-z A-z 0-9]+)$', views.followers.as_view()),
    url(r'^api/following1/(?P<user_id>[a-z A-z 0-9]+)$', views.following.as_view()),
    path('users/', include('registration.urls')),

    # jwt - start

    # url(r'^api/v1/auth/obtain_token/', obtain_jwt_token),
    # url(r'^api/v1/auth/refresh_token/', refresh_jwt_token),
    # The rest of the endpoints
    #url(r'^api/v1/', include('project.api', namespace='apiv1')),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),

    # jwt - end

    path('home/',include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
