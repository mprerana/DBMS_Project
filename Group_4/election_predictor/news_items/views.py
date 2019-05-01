from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Article, Feed, Query
from authentication.models import Usertype
from .forms import FeedForm, RegionForm
from authentication.models import Profile
from .serializers import ArticleSerializer
from rest_framework import generics
import ssl
import feedparser
import datetime
import urllib.request as urllib2
import json
from rest_framework.permissions import IsAuthenticated  # <-- Here


class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    # permission_classes = (IsAuthenticated,)             # <-- And here
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@login_required
def articles_list(request):
    user = request.user
    user_profile = Profile.objects.get(profile__user__username=user)
    response = urllib2.urlopen('https://api.ipify.org/?format=json')
    data = json.load(response)
    ip = data['ip']
    response = urllib2.urlopen(
        'http://api.db-ip.com/addrinfo?api_key=bc2ab711d740d7cfa6fcb0ca8822cb327e38844f&addr=' + str(ip))
    data = json.load(response)
    user_state = data['stateprov']
    user_location = user_state.replace(" ", "+")
    # user_location = user_profile.location
    q = user_location + 'election'
    k = Feed.objects.filter(query__query=q)
    k.delete()
    l = Query.objects.filter(query=q)
    l.delete()
    url = "https://news.google.com/rss?/search?cf=all&pz=1&q=" + q + "&hl=en-IN&gl=IN&ceid=IN:en"
    existingFeed = Feed.objects.filter(url=url)
    que = Query()
    que.query = q
    que.query_fk = Usertype.objects.get(user=request.user)
    feed = Feed()
    feed.url = url
    if len(existingFeed) == 0:
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        feedData = feedparser.parse(feed.url)
        # set some fields
        feed.title = feedData.feed.title
        feed.query = que
        que.save()
        feed.save()
        i = 0
        for entry in feedData.entries:
            if i > 20:
                break
            article = Article()
            article.title = entry.title
            article.url = entry.link
            article.description = entry.description

            d = datetime.datetime(*(entry.published_parsed[0:6]))
            dateString = d.strftime('%Y-%m-%d %H:%M:%S')

            article.publication_date = dateString
            article.feed = feed
            try:
                article.save()
            except:
                pass
            i = i + 1
    articles = Article.objects.filter(feed__url=url)
    rows = [articles[x:x + 1] for x in range(0, len(articles), 1)]
    return render(request, 'news_items/articles_list.html', {'rows': rows})


@login_required
def feeds_list(request):
    user_profile = Profile.objects.get(profile__user__username=request.user)
    articles = Article.objects.filter(feed__query__query_fk__user=user_profile.profile)
    rows = [articles[x:x + 1] for x in range(0, len(articles), 1)]
    return render(request, 'news_items/articles_list_feeds.html', {'rows': rows})


@login_required
def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        k = Feed.objects.filter(query__query=form.data['query'])
        k.delete()
        l = Query.objects.filter(query=form.data['query'])
        l.delete()

        if form.is_valid():
            feed = form.save(commit=False)
            q = feed.query
            # url = "https://news.google.com/rss/search?cf=all&pz=1&q="+q+"&hl=en-US&gl=US&ceid=US:en"
            url = "https://news.google.com/rss?/search?cf=all&pz=1&q=" + q + "&hl=en-IN&gl=IN&ceid=IN:en"
            existingFeed = Feed.objects.filter(url=url)
            que = Query()
            que.query = feed.query
            que.query_fk = Usertype.objects.get(user=request.user)
            feed = Feed()
            feed.url = url
            if len(existingFeed) == 0:
                if hasattr(ssl, '_create_unverified_context'):
                    ssl._create_default_https_context = ssl._create_unverified_context
                feedData = feedparser.parse(feed.url)
                # set some fields
                feed.title = feedData.feed.title
                feed.query = que
                que.save()
                feed.save()
                i = 0
                for entry in feedData.entries:
                    if i > 10:
                        break
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    try:
                        article.save()
                    except:
                        pass
                    i = i + 1
            articles = Article.objects.filter(feed__url=url)
            rows = [articles[x:x + 1] for x in range(0, len(articles), 1)]
            return render(request, 'news_items/search_results.html', {'rows': rows})
    else:
        form = FeedForm()
    return render(request, 'news_items/new_feed.html', {'form': form})


@login_required
def saved_queries(request):
    if request.method == "POST":
        query = request.POST.get('delete')
        if query:
            f = Article.objects.filter(feed__query__query=query)
            f.delete()
            a = Feed.objects.filter(query__query=query)
            a.delete()
            r = Query.objects.filter(query=query)
            r.delete()

    savedqps = Query.objects.filter(query_fk__user=request.user)
    return render(request, 'news_items/queries_saved.html', {'savedqps': savedqps})


@login_required
def regional_news(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        k = Feed.objects.filter(query__query=form.data['region'])
        k.delete()
        l = Query.objects.filter(query=form.data['region'])
        l.delete()

        if form.is_valid():
            feed = form.save(commit=False)
            q = feed.region
            url = "https://news.google.com/rss?/search?cf=all&pz=1&q=" + q + "&hl=en-IN&gl=IN&ceid=IN:en"
            existingFeed = Feed.objects.filter(url=url)
            que = Query()
            que.query = feed.region
            que.query_fk = Usertype.objects.get(user=request.user)
            feed = Feed()
            feed.url = url
            if len(existingFeed) == 0:
                if hasattr(ssl, '_create_unverified_context'):
                    ssl._create_default_https_context = ssl._create_unverified_context
                feedData = feedparser.parse(feed.url)
                # set some fields
                feed.title = feedData.feed.title
                feed.query = que
                que.save()
                feed.save()
                i = 0
                for entry in feedData.entries:
                    if i > 15:
                        break
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    try:
                        article.save()
                    except:
                        pass
                    i = i + 1
            articles = Article.objects.filter(feed__url=url)
            rows = [articles[x:x + 1] for x in range(0, len(articles), 1)]
            return render(request, 'news_items/regional_news_results.html', {'rows': rows})
    else:
        form = RegionForm()
    return render(request, 'news_items/regional_news.html', {'form': form})


@login_required
def national_news(request):
    q = 'national+election'
    k = Feed.objects.filter(query__query=q)
    k.delete()
    l = Query.objects.filter(query=q)
    l.delete()
    url = "https://news.google.com/rss?/search?cf=all&pz=1&q=" + q + "&hl=en-IN&gl=IN&ceid=IN:en"
    existingFeed = Feed.objects.filter(url=url)
    que = Query()
    que.query = q
    que.query_fk = Usertype.objects.get(user=request.user)
    feed = Feed()
    feed.url = url
    if len(existingFeed) == 0:
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        feedData = feedparser.parse(feed.url)
        # set some fields
        feed.title = feedData.feed.title
        feed.query = que
        que.save()
        feed.save()
        i = 0
        for entry in feedData.entries:
            if i > 20:
                break
            article = Article()
            article.title = entry.title
            article.url = entry.link
            article.description = entry.description

            d = datetime.datetime(*(entry.published_parsed[0:6]))
            dateString = d.strftime('%Y-%m-%d %H:%M:%S')

            article.publication_date = dateString
            article.feed = feed
            try:
                article.save()
            except:
                pass
            i = i + 1
    articles = Article.objects.filter(feed__url=url)
    rows = [articles[x:x + 1] for x in range(0, len(articles), 1)]
    return render(request, 'news_items/national_news.html', {'rows': rows})
