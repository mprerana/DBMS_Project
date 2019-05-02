from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.db import connection
import json
from collections import OrderedDict
import datetime
from django.db.models import DateTimeField


# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer

# class RatingViewSet(APIView):

#     def get(self, request, pk):
#         pklist = pk.split('n')
#         pk1 = int(pklist[0])
#         pk2 = int(pklist[1])
#         print(pk1)
#         print(pk2)
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT * FROM opinion_rating where user_id= %s and book_id= %s", [pk1, pk2])
#             tupleofratings = cursor.fetchall()

#             print(tupleofratings)

#             listofratings=[]

#             for tupleoflist  in tupleofratings:

#                 listofratings.append( OrderedDict(
#                     [('id', tupleoflist[0]),
#                     ('rating', tupleoflist[1]),
#                     ('timestamp', tupleoflist[2]),
#                     ('book_id', tupleoflist[3]),
#                     ('user_id', tupleoflist[4])
#                     ]))

#         return Response(listofratings)

class RatingViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM opinion_rating where book_id= %s", [pk])
            tupleofratings = cursor.fetchall()

            print(tupleofratings)

            listofratings=[]

            for tupleoflist  in tupleofratings:

                listofratings.append( OrderedDict(
                    [('id', tupleoflist[0]),
                    ('rating', tupleoflist[1]),
                    ('timestamp', tupleoflist[2]),
                    ('book_id', tupleoflist[3]),
                    ('user_id', tupleoflist[4])
                    ]))

        return Response(listofratings)

class RatingPostViewSet(APIView):
    

    def post(self, request, pk):
        time = datetime.datetime.now()
        time = str(time)

        data = request.data.get('addrating')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO opinion_rating ( rating,timestamp ,book_id ,user_id ) VALUES( %s,%s,%s,%s )",
                 [data['rating'], time, data['book_id'] ,pk ])
            
            cursor.execute(
                "SELECT * FROM opinion_rating WHERE user_id = %s AND book_id= %s", [pk,data['book_id']] )

            ratinglist = cursor.fetchone()

            insertedlist = OrderedDict(
                [('id', ratinglist[0]),
                 ('rating', ratinglist[1]),
                 ('timestamp', ratinglist[2]),
                 ('book_id', ratinglist[3]),
                 ('user_id', ratinglist[4])
                 ])

        return Response(insertedlist)

class ReviewViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM opinion_review where book_id= %s", [pk])
            tupleofreviews = cursor.fetchall()

            print(tupleofreviews)

            listofreviews=[]

            for tupleoflist  in tupleofreviews:

                listofreviews.append( OrderedDict(
                    [('id', tupleoflist[0]),
                    ('timestamp', tupleoflist[1]),
                    ('content', tupleoflist[2]),
                    ('book_id', tupleoflist[3]),
                    ('user_id', tupleoflist[4])
                    ]))

        return Response(listofreviews)

class ReviewPostViewSet(APIView):
    def post(self, request, pk):
        time = datetime.datetime.now()
        time = str(time)
        data = request.data.get('addreview')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO opinion_review ( content,timestamp, book_id,user_id ) VALUES( %s, %s, %s, %s )",
                 [data['content'],time, data['book_id'], pk ])
            
            cursor.execute(
                "SELECT * FROM opinion_review WHERE user_id = %s AND book_id= %s", [pk, data['book_id']] )

            reviewlist = cursor.fetchone()

            insertedlist = OrderedDict(
                [('id', reviewlist[0]),
                 ('timestamp', reviewlist[1]),
                 ('content', reviewlist[2]),
                 ('book_id', reviewlist[3]),
                 ('user_id', reviewlist[4])
                 ])

        return Response(insertedlist)



# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


