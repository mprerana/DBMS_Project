from rest_framework import serializers
from .models import *
from django.core.files import File
import base64


class movieSerializer(serializers.ModelSerializer):
    movie_poster_1 = serializers.SerializerMethodField()
    movie_poster_2= serializers.SerializerMethodField()
    class Meta:
        model = movie
        fields=['id','movie_name','movie_genre','movie_release_date','movie_age_rating','movie_duration_mins','movie_language','movie_actors','movie_directors','movie_producers','movie_writers','imdb_movie_rating','movie_description','movie_trailer_link','movie_poster_1','movie_poster_2']
        read_only_fields=('id','movie_name','movie_genre','movie_release_date','movie_age_rating','movie_duration_mins','movie_language','movie_actors','movie_directors','movie_producers','movie_writers','imdb_movie_rating','movie_description','movie_trailer_link','movie_poster_1','movie_poster_2')

    def get_movie_poster_1(self, obj):
        f = open(obj.movie_poster_1.path, 'rb')
        image = File(f)
        data = base64.encodestring(image.read())
        f.close()
        return data
    def get_movie_poster_2(self, obj):
        f = open(obj.movie_poster_2.path, 'rb')
        image = File(f)
        data = base64.encodestring(image.read())
        f.close()
        return data

class theatreSerializer(serializers.ModelSerializer):

    class Meta:
        model = theatre
        fields = ['id','theatre_name','adressline1','adressline2','city','state','pincode','theatre_rating','no_of_screens']
        read_only_fields=('id','theatre_name','adressline1','adressline2','city','state','pincode','theatre_rating','no_of_screens')


class screenSerializer(serializers.ModelSerializer):

    class Meta:
        model = screen
        fields=['id','theatre_id', 'screen_no', 'seat_string']
        read_only_fields = ( 'id','theatre_id', 'screen_no', 'seat_string')


class ticketSerializer(serializers.ModelSerializer):
    screen_id = screenSerializer()
    movie_id = movieSerializer()
    class Meta:
        model = ticket_price_and_time
        fields=['id','screen_id','movie_id','show_timings','date','language','screen_type','seat_class','price']
        read_only_fields=('id','screen_id','movie_id','show_timings','date','language','screen_type','seat_class','price')


class bookedticketSerializer(serializers.ModelSerializer):
    movie_details = ticketSerializer()

    class Meta:
        model = booked_tickets
        fields = ['ticket_seat_no', 'movie_details', 'ticket_book_from', 'ticket_booking_website',
                  'ticket_booking_tranc_id', 'ticket_booking_username', 'name', 'phone_number', 'email', 'ticked_id', ]
        write_only_fields = (
        'ticket_book_from', 'ticket_booking_website', 'ticket_booking_tranc_id', 'ticket_booking_username', 'name',
        'phone_number', 'email', 'ticked_id',)


class updatemovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_update
        fields = ['movie_id', 'last_change']
        read_only_fields = ('movie_id', 'last_change')


class updatetheatreSerializer(serializers.ModelSerializer):
        class Meta:
            model = changes_on_theaters
            fields = [ 'theatre_id','last_change','change_type' ]
            read_only_fields = ('theatre_id','last_change','change_type')


class updatescreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = changes_on_screens
        fields = ['screen_id', 'last_change', 'change_type']
        read_only_fields = ('screen_id', 'last_change', 'change_type')


class updateticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket_update
        fields = ['ticket_price_and_time_id', 'last_change',]
        read_only_fields = ('ticket_price_and_time_id', 'last_change',)

