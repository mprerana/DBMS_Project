from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('create_story/', views.blog_display, name='blog'),
    path('stories/', views.home, name='home'),
    url(r'^stories/(?P<blog_id>[0-9]+)$', views.show_blog, name='show_blog'),
    url(r'^stories/(?P<blog_id>[0-9]+)/like$', views.BlogLikeRedirect.as_view(), name='like'),
    path('name-autocomplete/', views.InterestAutocomplete.as_view(), name='name-autocomplete'),
    url(r'^api/stories/(?P<blog_id>[0-9]+)/like$', views.BlogLikeAPI.as_view(), name='api_like'),
]
