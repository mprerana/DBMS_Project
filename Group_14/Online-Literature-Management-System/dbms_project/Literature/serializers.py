from rest_framework import serializers
from .models import *
from User.serializers import UserSerializer


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'work_title', 'author', 'uploader', 'description', 'timestamp', 'genre', 'thumbnail',
                  'file',)


class UserWorkSerializer(serializers.ModelSerializer):
    work_user = WorkSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',)

    def create(self, validated_data):
        works_data = validated_data.pop('work_user')
        user = User.objects.create(**validated_data)
        for work_data in works_data:
            Work.objects.create(uploader=user, **work_data)
        return user


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'uploader', 'blog_title', 'blog_content', 'timestamp',)


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ('id', 'r_list_name', 'related_user', 'books',)


class UserReadingListSerializer(serializers.ModelSerializer):
    readinglist_user = ReadingListSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)

    def create(self, validated_data):
        readinglists_data = validated_data.pop('readinglist_user')
        user = User.objects.create(**validated_data)
        for readinglist_data in readinglists_data:
            ReadingList.objects.create(related_user=user, **readinglist_data)
        return user
