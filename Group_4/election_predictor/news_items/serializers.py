from rest_framework import serializers
from .models import Article, Feed, Query

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'url', 'description', 'publication_date')