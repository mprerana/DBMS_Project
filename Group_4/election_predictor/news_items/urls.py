from django.conf.urls import url
from . import views
from .views import ListArticleView
from django.urls import path


app_name = 'news_items'

urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^feeds/new', views.new_feed, name='feed_new'),
    url(r'^feeds/', views.feeds_list, name='feeds_list'),
    url(r'^saved_queries', views.saved_queries, name='saved_queries'),
    url(r'^regional_news', views.regional_news, name='regional_news'),
    url(r'^national_news', views.national_news, name='national_news'),
    path('articles/', ListArticleView.as_view(), name="articles-all"),

]
