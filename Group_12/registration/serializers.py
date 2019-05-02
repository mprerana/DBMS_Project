from rest_framework import serializers
from .models import  Follower
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        User1 = User.objects.create(username=username, email=email, password=password)#cover_photo=cover_photo)
        return User1

