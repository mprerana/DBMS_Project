from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class USERSerializer(serializers.ModelSerializer):

    user_data = UserSerializer(required=True)

    class Meta:
        model = USER
        fields = ('id', 'user_data', 'dob', 'image', 'mobile_no',)

    def create(self, validated_data):
        userdata = validated_data.pop('user_data')
        user_data = UserSerializer.create(UserSerializer(), validated_data=userdata)

        user, created = USER.objects.update_or_create(user_data= user_data, id= validated_data.pop('id'),
                                                       dob= validated_data.pop('dob'), image=validated_data.pop('image'),
                                                        mobile_no=validated_data.pop('mobile_no'),)

        return user





class FOLLOWSerializer(serializers.ModelSerializer):
    class Meta:
        model = FOLLOW
        fields = ('id', 'user', 'follower')
