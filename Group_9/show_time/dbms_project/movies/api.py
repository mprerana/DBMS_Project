from movies.models import Movies, testmodel

from .serializers import MoviesSerializer, TestSerializer

from rest_framework import viewsets, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import json
from collections import OrderedDict

from django.shortcuts import get_object_or_404

import random

# movieViewset


class MoviesView(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_movies")
            cursor.execute(
                "select movies_movies.id,movies_movies.title,movies_movies.release_date,movies_movies.censor_rating,movies_movies.image_source,movies_movies.synopsis,movies_movies.trailer_link,movies_movies.time_duration,movies_movies.likes,movies_movies.status from movies_city_movie inner join movies_cities on movies_city_movie.city_id=movies_cities.id inner join movies_movies on movies_city_movie.movie_title_id=movies_movies.id where movies_city_movie.city_id=%s ", [pk])
            tupleofmovies = cursor.fetchall()

            listofmovies = []

            for i in tupleofmovies:

                k = ''

                for j in i[8]:
                    if(j != ' ' and j != ','):
                        k = k+j

                # print(int(k))

                only_movie = OrderedDict(
                    [('id', i[0]),
                     ('title', i[1]),
                     ('release_date', i[2]),
                     ('censor_rating', i[3]),
                     ('image_source', i[4]),
                     ('synopsis', i[5]),
                     ('trailer_link', i[6]),
                     ('time_duration', i[7]),
                     ('likes', int(k)),
                     ('status', i[9])
                     ])

                cursor.execute(
                    "SELECT movies_genre.id,genre FROM movies_genre INNER JOIN movies_genre_movie on movies_genre.id = movies_genre_movie.movie_genre_id WHERE title_id = %s", [i[0]])
                tupleofgenre = cursor.fetchall()

                allgenre = []

                for j in tupleofgenre:
                    genre = OrderedDict(
                        [('id', j[0]),
                         ('genre', j[1]),
                         ])

                    allgenre.append(genre)

                only_movie.update({"allgenre": allgenre})

                cursor.execute(
                    "SELECT movies_languages.id,language FROM movies_languages INNER JOIN movies_language_movie on movies_languages.id = movies_language_movie.movie_language_id  WHERE title_id = %s", [i[0]])
                tupleoflanguages = cursor.fetchall()

                allanguages = []

                for j in tupleoflanguages:
                    language = OrderedDict(
                        [('id', j[0]),
                         ('language', j[1]),
                         ])

                    allanguages.append(language)

                only_movie.update({"allanguages": allanguages})

                cursor.execute(
                    "SELECT movies_formats.id,mformat FROM movies_formats INNER JOIN movies_format_movie on movies_formats.id = movies_format_movie.movie_format_id  WHERE title_id = %s", [i[0]])
                tupleofformats = cursor.fetchall()

                allformats = []

                for j in tupleofformats:
                    format = OrderedDict(
                        [('id', j[0]),
                         ('format', j[1]),
                         ])

                    allformats.append(format)

                only_movie.update({"allformats": allformats})

                listofmovies.append(only_movie)

        return Response(listofmovies)

    # def put(self, request, pk):
    #     #saved_article = get_object_or_404(Movies.objects.all(), pk=pk)
    #     data = request.data
    #     print(data)
    #     return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})


class MoviesCompleteView(APIView):
    def get(self, request, pk):

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_movies where id= %s", [pk])
            tupleofmovie = cursor.fetchone()

            moviecompletedetail = OrderedDict(
                [('id', tupleofmovie[0]),
                 ('title', tupleofmovie[1]),
                 ('release_date', tupleofmovie[2]),
                 ('censor_rating', tupleofmovie[3]),
                 ('image_source', tupleofmovie[4]),
                 ('synopsis', tupleofmovie[5]),
                 ('trailer_link', tupleofmovie[6]),
                 ('time_duration', tupleofmovie[7]),
                 ('likes', tupleofmovie[8]),
                 ('status', tupleofmovie[9])
                 ])

            cursor.execute(
                "SELECT movies_cast_crew.id,castname,image FROM movies_cast_crew INNER JOIN movies_cast_crew_movie on movies_cast_crew.id = movies_cast_crew_movie.cast_crew_id WHERE title_id = %s", [pk])
            tupleofcast = cursor.fetchall()

            completecast = []

            for i in tupleofcast:
                cast = OrderedDict(
                    [('id', i[0]),
                     ('cast', i[1]),
                     ('image', i[2])
                     ])

                completecast.append(cast)

            moviecompletedetail.update({"completecast": completecast})

            cursor.execute(
                "SELECT movies_genre.id,genre FROM movies_genre INNER JOIN movies_genre_movie on movies_genre.id = movies_genre_movie.movie_genre_id WHERE title_id = %s", [pk])
            tupleofgenre = cursor.fetchall()

            allgenre = []

            for i in tupleofgenre:
                genre = OrderedDict(
                    [('id', i[0]),
                     ('genre', i[1]),
                     ])

                allgenre.append(genre)

            moviecompletedetail.update({"allgenre": allgenre})

            cursor.execute(
                "SELECT movies_languages.id,language FROM movies_languages INNER JOIN movies_language_movie on movies_languages.id = movies_language_movie.movie_language_id  WHERE title_id = %s", [pk])
            tupleoflanguages = cursor.fetchall()

            allanguages = []

            for i in tupleoflanguages:
                language = OrderedDict(
                    [('id', i[0]),
                     ('language', i[1]),
                     ])

                allanguages.append(language)

            moviecompletedetail.update({"allanguages": allanguages})

            cursor.execute(
                "SELECT movies_formats.id,mformat FROM movies_formats INNER JOIN movies_format_movie on movies_formats.id = movies_format_movie.movie_format_id  WHERE title_id = %s", [pk])
            tupleofformats = cursor.fetchall()

            allformats = []

            for i in tupleofformats:
                format = OrderedDict(
                    [('id', i[0]),
                     ('format', i[1]),
                     ])

                allformats.append(format)

            moviecompletedetail.update({"allformats": allformats})

            cursor.execute(
                "SELECT id,user_id,ratestatus,rating,comment FROM movies_rating WHERE title_id = %s", [pk])
            tupleofcomment = cursor.fetchall()

            allcomments = []

            for i in tupleofcomment:
                cursor.execute(
                    "SELECT username FROM auth_user WHERE id = %s", [i[1]])
                username = cursor.fetchone()

                comment = OrderedDict(
                    [('id', i[0]),
                     ('user', username[0]),
                     ('ratestatus', i[2]),
                     ('rating', i[3]),
                     ('comment', i[4]),
                     ])

                allcomments.append(comment)

            moviecompletedetail.update({"allcomments": allcomments})

        return Response(moviecompletedetail)


class LikeUpdateView(APIView):
    def put(self, request, pk):
        data = request.data.get('likes')
        print(data)
        print(type(data))

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE movies_movies SET likes=%s WHERE id=%s", [data['likes'], pk])
            cursor.execute(
                "SELECT * FROM movies_movies WHERE id = %s", [pk])
            likeupdate = cursor.fetchone()

            print(likeupdate[0])

            updatedmovie = OrderedDict(
                [('id', likeupdate[0]),
                 ('title', likeupdate[1]),
                 ('release_date', likeupdate[2]),
                 ('censor_rating', likeupdate[3]),
                 ('image_source', likeupdate[4]),
                 ('synposis', likeupdate[5]),
                 ('trailer_link', likeupdate[6]),
                 ('time_duration', likeupdate[7]),
                 ('likes', likeupdate[8]),
                 ('status', likeupdate[9])
                 ])

        return Response(updatedmovie)


class PostRatingView(APIView):
    def post(self, request):
        data = request.data.get('rating')
        ratestatus = 1

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_rating WHERE title_id = %s and  user_id= %s", [data['title'], data['user']])

            rating = cursor.fetchone()

            if(rating):
                type(rating)

            else:
                cursor.execute(
                    "INSERT INTO movies_rating (title_id,user_id,ratestatus,rating,comment) VALUES( %s, %s,%s, %s,%s)", [data['title'], data['user'], ratestatus, data['rating'], data['comment']])
                cursor.execute(
                    "SELECT * FROM movies_rating WHERE title_id = %s and  user_id= %s", [data['title'], data['user']])

                rating = cursor.fetchone()

            print(rating)

            insertedrating = OrderedDict(
                [('id', rating[0]),
                 ('ratestatus', rating[1]),
                 ('rating', rating[2]),
                 ('comment', rating[3]),
                 ('title_id', rating[4]),
                 ('user_id', rating[5]),
                 ])

        return Response(insertedrating)


class TestView(APIView):
    def get(self, request):
        tests = testmodel.objects.raw('SELECT * FROM movies_testmodel')

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_testmodel")
            # print(cursor.fetchone())
            tt = cursor.fetchall()
            print(".....hello", tt)

            listoftests = []

            for i in tt:

                listoftests.append(OrderedDict(
                    [('id', i[0]), ('title', i[1]), ('genre', i[2])]))

            print('happpyaqwerty', listoftests)

            k = json.dumps(listoftests)

            print('......k.....', k)

            # print(typek)

        serializer = TestSerializer(tests, many=True)

        print(serializer.data)

        return Response(listoftests)

    def put(self, request, pk):

        saved_testmodel = get_object_or_404(testmodel.objects.all(), pk=pk)
        data = request.data.get('testmodel')
        serializer = TestSerializer(
            instance=saved_testmodel, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})


class TestPutView(APIView):
    def put(self, request, pk):

        saved_testmodel = get_object_or_404(testmodel.objects.all(), pk=pk)
        data = request.data.get('testmodel')
        print(data)
        print(type(data))

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE movies_testmodel SET title=%s,genre=%s WHERE id=%s", [data['title'], data['genre'], pk])
            cursor.execute(
                "SELECT * FROM movies_testmodel WHERE id = %s", [pk])
            tt = cursor.fetchone()
            print(".....hello", tt)

        # serializer = TestSerializer(
        #     instance=saved_testmodel, data=data, partial=True)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(tt)})


class allgenresView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,genre FROM movies_genre")
            tupleofgenre = cursor.fetchall()

            allgenre = []

            for i in tupleofgenre:
                genre = OrderedDict(
                    [('id', i[0]),
                     ('genre', i[1]),
                     ])

                allgenre.append(genre)

        return Response(allgenre)


class allanguagesView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,language FROM movies_languages")
            tupleoflanguage = cursor.fetchall()

            allanguage = []

            for i in tupleoflanguage:
                language = OrderedDict(
                    [('id', i[0]),
                     ('language', i[1]),
                     ])

                allanguage.append(language)

        return Response(allanguage)


class allformatsView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,mformat FROM movies_formats")
            tupleofformats = cursor.fetchall()

            allformats = []

            for i in tupleofformats:
                formats = OrderedDict(
                    [('id', i[0]),
                     ('format', i[1]),
                     ])

                allformats.append(formats)

        return Response(allformats)


class allSnacksView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,snacks,image,cost FROM movies_theatre_snacks")
            tupleofsnacks = cursor.fetchall()

            allsnacks = []

            for i in tupleofsnacks:

                snack = OrderedDict(
                    [('id', i[0]),
                     ('snacks', i[1]),
                     ('image', i[2]),
                     ('price', i[3])
                     ])

                allsnacks.append(snack)

        return Response(allsnacks)


class BookingPageCompleteView(APIView):
    def get(self, request, movie_id, city_id):

        with connection.cursor() as cursor:
            cursor.execute(
                "select m.title, m.image_source, m.time_duration, m.likes from movies_movies as m where m.id=%s", [movie_id])
            tupleofmovie = cursor.fetchone()

            movie = OrderedDict(
                [('movie', tupleofmovie[0]),
                 ('image_source', tupleofmovie[1]),
                 ('time_duration', tupleofmovie[2]),
                 ('likes', tupleofmovie[3])
                 ])

            with connection.cursor() as cursor:
                cursor.execute(
                    " select distinct cast.id, cast.castname, cast.image from movies_cast_crew as cast inner join movies_cast_crew_movie as castmovie on cast.id = castmovie.cast_crew_id inner join movies_movies as m on castmovie.title_id =m.id and m.id=%s", [movie_id])
                tupleofcast = cursor.fetchall()
                listofcasts = []

                for j in tupleofcast:
                    cast = OrderedDict(
                        [('cast_id', j[0]),
                         ('castname', j[1]),
                         ('cast_image', j[2]),
                         ])
                    listofcasts.append(cast)

            movie.update({"castDetails": listofcasts})

            with connection.cursor() as cursor:
                cursor.execute(
                    " select g.id, g.genre from movies_genre_movie as gm inner join movies_movies as m on gm.title_id =m.id and m.id=%s inner join movies_genre as g on g.id=gm.movie_genre_id", [movie_id])
                tupleofgenre = cursor.fetchall()
                listofgenres = []

                for i in tupleofgenre:
                    genre = OrderedDict(
                        [('genre_id', i[0]),
                         ('genre', i[1]),
                         ])

                    listofgenres.append(genre)

            movie.update({"genreDetails": listofgenres})

            with connection.cursor() as cursor:
                cursor.execute(
                    " select distinct t.id, c.city, t.theatre_name, s.date from movies_theatre_showtimings as s inner join movies_city_theatre as t on t.id = s.citytheatre_id inner join movies_cities as c on c.id=t.city_id and c.id= %s inner join movies_movies as m on m.id = s.title_id and m.id = %s", [city_id, movie_id])
                tupleoftheatre = cursor.fetchall()
                theatre = []
                finallist = []

                for i in tupleoftheatre:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            " select l.id, l.language from movies_theatre_showtimings as s inner join movies_city_theatre as t on t.id = s.citytheatre_id inner join movies_cities as c on c.id=t.city_id and c.id= %s inner join movies_movies as m on m.id = s.title_id and m.id = %s inner join movies_languages as l on l.id=s.language_id and s.citytheatre_id=%s where  s.date=%s", [city_id, movie_id, i[0], i[3]])
                        tupleoflanguage = cursor.fetchall()
                        languages = []
                        for j in tupleoflanguage:
                            language = OrderedDict(
                                [('id', j[0]),
                                    ('language', j[1]),
                                 ])

                            languages.append(language)
                    with connection.cursor() as cursor:
                        cursor.execute(
                            " select f.id, f.mformat from movies_theatre_showtimings as s inner join movies_city_theatre as t on t.id = s.citytheatre_id inner join movies_cities as c on c.id=t.city_id and c.id= %s inner join movies_movies as m on m.id = s.title_id and m.id = %s inner join movies_formats as f on f.id=s.format_id and s.citytheatre_id=%s where  s.date=%s", [city_id, movie_id, i[0], i[3]])
                        tupleofformat = cursor.fetchall()
                        formats = []
                        for j in tupleofformat:
                            format = OrderedDict(
                                [('id', j[0]),
                                    ('format', j[1]),
                                 ])

                            formats.append(format)

                    with connection.cursor() as cursor:
                        cursor.execute(
                            " select s.id,s.show_timings from movies_theatre_showtimings as s inner join movies_city_theatre as t on t.id = s.citytheatre_id inner join movies_cities as c on c.id=t.city_id and c.id= %s inner join movies_movies as m on m.id = s.title_id and m.id = %s inner join movies_formats as f on f.id=s.format_id and s.citytheatre_id=%s where  s.date=%s", [city_id, movie_id, i[0], i[3]])
                        tupleoftimings = cursor.fetchall()
                        timings = []
                        for j in tupleoftimings:
                            timing = OrderedDict(
                                [
                                    ('show_id', j[0]),
                                    ('time', j[1]),
                                ])

                            timings.append(timing)

                    theatre.append(OrderedDict(
                        [('theatre_id', i[0]),
                            ('city', i[1]),
                            ('theatre', i[2]),
                            #  ('timings', i[3]),
                            # ('movie', i[3]),
                            #  ('language', i[5]),
                            #  ('format', i[6]),
                            ('date', i[3]),
                            ('language', languages),
                            ('format', formats),
                            ('timing', timings),
                         ]))
            movie.update({"theatreDetails": theatre})

        return Response(movie)


class GetBookingDetails(APIView):
    def get(self, request, user_id):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT b.title,  b.booking_id, b.city, b.theatre, b.cost, b.language, b.dimension, b.category, b.seat_no, b.timings, b.snacks , b.id FROM movies_booking_ticket as b where b.user_id= %s ", [user_id])
            tupleofbookedtickets = cursor.fetchall()

            tickets = {}
            ticketlist = []
            for i in tupleofbookedtickets:
                bookedticket = OrderedDict(
                    [('movie', i[0]),
                     ('booking_id', i[1]),
                     ('city', i[2]),
                     ('theatre', i[3]),
                     ('cost', i[4]),
                     ('language', i[5]),
                     ('dimension', i[6]),
                     ('category', i[7]),
                     ('seat_no', i[8]),
                     ('timings', i[9]),
                     ('snacks', i[10]),
                     ('id', i[11]),
                     ]
                )
                ticketlist.append(bookedticket)
            tickets.update({'tickets': ticketlist})

        return Response(tickets)


class allGetCities(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_cities")
            tupleofcities = cursor.fetchall()

            allcities = []
            for i in tupleofcities:
                city = OrderedDict(
                    [('id', i[0]),
                     ('city', i[1]),
                     ('status', 0),
                     ]
                )
                allcities.append(city)

        return Response(allcities)


# class allSnacksView(APIView):
#     def get(self, request):
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT id,snacks,image,cost FROM movies_theatre_snacks")
#             tupleofsnacks = cursor.fetchall()

#             allsnacks = []

#             for i in tupleofsnacks:

#                 snack = OrderedDict(
#                     [('id', i[0]),
#                      ('snacks', i[1]),
#                      ('image', i[2]),
#                      ('price', i[3])
#                      ])

#                 allsnacks.append(snack)

#         return Response(allsnacks)

class GetSpecificTheatreShowtimings(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT date,title_id,language_id,format_id,show_timings,id FROM movies_theatre_showtimings WHERE id=%s", [pk])
            tupleoftheatre = cursor.fetchone()

            # allshow = []

            cursor.execute(
                "SELECT title FROM movies_movies WHERE id=%s", [tupleoftheatre[1]])
            tupleofmovie = cursor.fetchone()

            cursor.execute(
                "SELECT language FROM movies_languages WHERE id=%s", [tupleoftheatre[2]])
            tupleoflanguage = cursor.fetchone()

            cursor.execute(
                "SELECT mformat FROM movies_formats WHERE id=%s", [tupleoftheatre[3]])
            tupleofformat = cursor.fetchone()

            # for i in tupleofsnacks:

            show = OrderedDict(
                [('date', tupleoftheatre[0]),
                 ('title', tupleofmovie[0]),
                 ('language', tupleoflanguage[0]),
                 ('format', tupleofformat[0]),
                 ('show_timings', tupleoftheatre[4]),
                 ('id', tupleoftheatre[5])
                 ])

        return Response(show)


class BookedSeats(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,seatno FROM movies_theatre_seats WHERE show_time_no_id=%s", [pk])
            tupleofbookedseats = cursor.fetchall()

            allbooks = []

            for i in tupleofbookedseats:

                snack = OrderedDict(
                    [('id', i[0]),
                     ('seatno', i[1])
                     ])

                allbooks.append(snack)

        return Response(allbooks)

# class PostRatingView(APIView):
#     def post(self, request):
#         data = request.data.get('rating')
#         ratestatus = 1

#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT * FROM movies_rating WHERE title_id = %s and  user_id= %s", [data['title'], data['user']])

#             rating = cursor.fetchone()

#             if(rating):
#                 type(rating)

#             else:
#                 cursor.execute(
#                     "INSERT INTO movies_rating (title_id,user_id,ratestatus,rating,comment) VALUES( %s, %s,%s, %s,%s)", [data['title'], data['user'], ratestatus, data['rating'], data['comment']])
#                 cursor.execute(
#                     "SELECT * FROM movies_rating WHERE title_id = %s and  user_id= %s", [data['title'], data['user']])

#                 rating = cursor.fetchone()

#             print(rating)

#             insertedrating = OrderedDict(
#                 [('id', rating[0]),
#                  ('ratestatus', rating[1]),
#                  ('rating', rating[2]),
#                  ('comment', rating[3]),
#                  ('title_id', rating[4]),
#                  ('user_id', rating[5]),
#                  ])

#         return Response(insertedrating)


class PostaSeatView(APIView):
    def post(self, request):
        data = request.data.get('posting')

        with connection.cursor() as cursor:

            cursor.execute(
                "INSERT INTO movies_theatre_seats (seatno,show_time_no_id) VALUES( %s, %s)", [data['seatno'], data['show_time_no_id']])
            cursor.execute(
                "SELECT * FROM movies_theatre_seats WHERE seatno = %s and  show_time_no_id= %s", [data['seatno'], data['show_time_no_id']])

            rating = cursor.fetchone()

            print(rating)

            insertedposting = OrderedDict(
                [('id', rating[0]),
                 ('seatno', rating[1]),
                 ('show_time_no_id', rating[2])
                 ])

        return Response(insertedposting)


class YourBookingPost(APIView):
    def post(self, request):
        data = request.data.get('posting')

        print(data)

        with connection.cursor() as cursor:

            cursor.execute(
                "INSERT INTO movies_booking_ticket (booking_id,title,city,theatre,cost,language,dimension,category,seat_no,timings,snacks,user_id) VALUES( %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)", [data['booking_id'], data['title'], data['city'],data['theatre'],data['cost'],data['language'],data['dimension'],data['category'],data['seat_no'],data['timings'],data['snacks'],data['user_id']])
            cursor.execute(
                "SELECT * FROM movies_booking_ticket")

            rating = cursor.fetchone()

           
        return Response({"response":"response is awesome"})


class ChatBotMoviesCompleteView(APIView):
    def get(self, request, pk):

        print(pk)
        print(type(pk))

        pk = "%"+pk+"%"

        print(pk)

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM movies_movies where title like %s", [pk])
            tupleofmovie = cursor.fetchone()

            movie_id = tupleofmovie[0]

            moviecompletedetail = OrderedDict(
                [('id', tupleofmovie[0]),
                 ('title', tupleofmovie[1]),
                 ('release_date', tupleofmovie[2]),
                 ('censor_rating', tupleofmovie[3]),
                 ('image_source', tupleofmovie[4]),
                 ('synopsis', tupleofmovie[5]),
                 ('trailer_link', tupleofmovie[6]),
                 ('time_duration', tupleofmovie[7]),
                 ('likes', tupleofmovie[8]),
                 ('status', tupleofmovie[9])
                 ])

            cursor.execute(
                "SELECT movies_cast_crew.id,castname,image FROM movies_cast_crew INNER JOIN movies_cast_crew_movie on movies_cast_crew.id = movies_cast_crew_movie.cast_crew_id WHERE title_id = %s", [movie_id])
            tupleofcast = cursor.fetchall()

            completecast = []

            for i in tupleofcast:
                cast = OrderedDict(
                    [('id', i[0]),
                     ('cast', i[1]),
                     ('image', i[2])
                     ])

                completecast.append(cast)

            moviecompletedetail.update({"completecast": completecast})

            cursor.execute(
                "SELECT movies_genre.id,genre FROM movies_genre INNER JOIN movies_genre_movie on movies_genre.id = movies_genre_movie.movie_genre_id WHERE title_id = %s", [movie_id])
            tupleofgenre = cursor.fetchall()

            allgenre = []

            for i in tupleofgenre:
                genre = OrderedDict(
                    [('id', i[0]),
                     ('genre', i[1]),
                     ])

                allgenre.append(genre)

            moviecompletedetail.update({"allgenre": allgenre})

            cursor.execute(
                "SELECT movies_languages.id,language FROM movies_languages INNER JOIN movies_language_movie on movies_languages.id = movies_language_movie.movie_language_id  WHERE title_id = %s", [movie_id])
            tupleoflanguages = cursor.fetchall()

            allanguages = []

            for i in tupleoflanguages:
                language = OrderedDict(
                    [('id', i[0]),
                     ('language', i[1]),
                     ])

                allanguages.append(language)

            moviecompletedetail.update({"allanguages": allanguages})

            cursor.execute(
                "SELECT movies_formats.id,mformat FROM movies_formats INNER JOIN movies_format_movie on movies_formats.id = movies_format_movie.movie_format_id  WHERE title_id = %s", [movie_id])
            tupleofformats = cursor.fetchall()

            allformats = []

            for i in tupleofformats:
                format = OrderedDict(
                    [('id', i[0]),
                     ('format', i[1]),
                     ])

                allformats.append(format)

            moviecompletedetail.update({"allformats": allformats})

            cursor.execute(
                "SELECT id,user_id,ratestatus,rating,comment FROM movies_rating WHERE title_id = %s", [movie_id])
            tupleofcomment = cursor.fetchall()

            allcomments = []

            for i in tupleofcomment:
                cursor.execute(
                    "SELECT username FROM auth_user WHERE id = %s", [i[1]])
                username = cursor.fetchone()

                comment = OrderedDict(
                    [('id', i[0]),
                     ('user', username[0]),
                     ('ratestatus', i[2]),
                     ('rating', i[3]),
                     ('comment', i[4]),
                     ])

                allcomments.append(comment)

            moviecompletedetail.update({"allcomments": allcomments})

        return Response(moviecompletedetail)
