from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.db import connection
import json
from collections import OrderedDict
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class AllUSERViewSet(viewsets.ModelViewSet):

    queryset = USER.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = USERSerializer

    # def get_queryset(self):
    #      return self.request.user.all()

    def perform_create(self, serializer):
        serializer.save(user_data=self.request.user)


class USERViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT username, first_name, last_name, email FROM auth_user where id= %s", [pk])

            user = cursor.fetchone()

            cursor.execute(
                "SELECT dob, image, mobile_no, bio FROM user_user where user_data_id= %s", [pk])

            userdetail = cursor.fetchone()

            userdata = OrderedDict(
                [('username', user[0]),
                 ('first_name', user[1]),
                 ('last_name', user[2]),
                 ('email', user[3]),
                 ('dob', userdetail[0]),
                 ('image', userdetail[1]),
                 ('mobile_no', userdetail[2]),
                 ('bio', userdetail[3])
                 ])

        return Response(userdata)


class USERPutViewSet(APIView):
    def put(self, request, pk):
        data = request.data.get('newdetails')
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE  auth_user SET email=%s,first_name=%s,last_name=%s WHERE id=%s",
                [data['email'], data['first_name'], data['last_name'], pk])

            cursor.execute(
                "SELECT username,email,first_name,last_name FROM auth_user WHERE id=%s", [pk])
            currentuser = cursor.fetchone()

            cursor.execute(
                "UPDATE  user_user SET dob=%s,image=%s,mobile_no=%s,bio=%s WHERE user_data_id=%s",
                [data['dob'], data['image'], data['mobile_no'], data['bio'], pk])

            cursor.execute(
                "SELECT dob,image,mobile_no,bio FROM user_user WHERE user_data_id=%s", [pk])
            currentuserprofile = cursor.fetchone()

            userdetails = OrderedDict(
                [('username', currentuser[0]),
                 ('email', currentuser[1]),
                 ('first_name', currentuser[2]),
                 ('last_name', currentuser[3]),
                 ('dob', currentuserprofile[0]),
                 ('image', currentuserprofile[1]),
                 ('mobile_no', currentuserprofile[2]),
                 ('bio', currentuserprofile[3]),
                 ])

        return Response(userdetails)


class FOLLOWViewSet(viewsets.ModelViewSet):
    queryset = FOLLOW.objects.all()
    serializer_class = FOLLOWSerializer


class GetFollowersViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM auth_user where id=%s", [pk]
            )
            user = cursor.fetchone()

            follower = OrderedDict(
                [('id', user[0])]
            )

            cursor.execute(
                "SELECT * FROM user_follow where user_id= %s", [pk])

            allfollowers = cursor.fetchall()

            followers = []

            for tupleoffollowers in allfollowers:
                cursor.execute(
                    "SELECT username FROM auth_user where id= %s", [tupleoffollowers[1]])

                user = cursor.fetchone()
                followers.append(OrderedDict(
                    [
                        ('id', tupleoffollowers[0]),
                        ('follower_id', tupleoffollowers[1]),
                        ('user', user[0]),

                    ]))

            follower.update({"followers": followers})

        return Response(follower)


class GetFollowingViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM auth_user where id=%s", [pk]
            )
            user = cursor.fetchone()

            userfollowing = OrderedDict(
                [('id', user[0]),
                 ]
            )

            cursor.execute(
                "SELECT * FROM user_follow where follower_id= %s", [pk])

            allfollowing = cursor.fetchall()

            following = []

            for tupleoffollowers in allfollowing:
                cursor.execute(
                    "SELECT username FROM auth_user where id= %s", [tupleoffollowers[2]])

                user = cursor.fetchone()

                following.append(OrderedDict(
                    [
                        ('id', tupleoffollowers[0]),
                        ('following_id', tupleoffollowers[2]),
                        ('user', user[0]),


                    ]))

            userfollowing.update({"following": following})

        return Response(userfollowing)


class FollowViewSet(APIView):
    def post(self, request, pk):
        pklist = pk.split('n')
        pk1 = pklist[0]
        pk2 = pklist[1]
        data = request.data.get('follow')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user_follow ( user_id,follower_id ) VALUES( %s,%s )",
                [pk1, pk2])

            cursor.execute(
                "SELECT * FROM user_follow WHERE follower_id = %s AND user_id= %s",
                [pk2, pk1])

            follow = cursor.fetchone()

            insertedfollow = OrderedDict(
                [('id', follow[0]),
                 ('follower_id', follow[1]),
                 ('user_id', follow[2]),
                 ])

        return Response(insertedfollow)


class UnFollowViewSet(APIView):
    def delete(self, request, pk):
        pklist = pk.split('n')
        pk1 = pklist[0]
        pk2 = pklist[1]
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM user_follow WHERE user_id=%s AND follower_id=%s",
                [pk1, pk2])

        return Response(pk)
