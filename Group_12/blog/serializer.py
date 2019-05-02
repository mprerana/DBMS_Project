from rest_framework import serializers
from .models import interest, Blog, Comment
from django.contrib.auth.models import User

class interestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'heading', 'content', 'upvotes', 'post_date', 'interests','cover_photo')

    def create(self, validated_data):
        author = validated_data['author']
        heading = validated_data['heading']
        #draft = validated_data['draft']
        content = validated_data['content']
        # upvotes = validated_data['upvotes']
        # post_date=validated_data['post_date']
        interests = validated_data['interests']
        #cover_photo = validated_data['cover_photo']
        qs = interest.objects.filter(interest_name=interests)
        print(interests)
        if qs.exists():
            interest_var = interest.objects.get(interest_name=interests)
            Blog1 = Blog.objects.create(author=author, heading=heading, content=content,
                                        interests=interest_var)#cover_photo=cover_photo)
            return Blog1


class bloginterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = interest
        fields = ('interest_name',)

class blogauthorserealizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
class BlogSerializer(serializers.ModelSerializer):
    interests = bloginterestSerializer()
    author = blogauthorserealizer()
    class Meta:
        model = Blog
        fields = ('id','author', 'heading', 'content', 'upvotes', 'post_date', 'interests','cover_photo')

