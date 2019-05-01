from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class movie_data(APIView):

    def get(self, request):
        movies = movie.objects.all()
        serializer = movieSerializer(movies, many=True)
        return Response(serializer.data)


class theatre_data(APIView):

    def get(self,request):
        theatres=theatre.objects.all()
        serializer=theatreSerializer(theatres,many=True)
        return Response(serializer.data)

class screen_data(APIView):

    def get(self,request):
        screens=screen.objects.all()
        serializer=screenSerializer(screens,many=True)
        return Response(serializer.data)


class ticket_data(APIView):

    def get(self, request):
        tickets = ticket_price_and_time.objects.all()
        serializer = ticketSerializer(tickets, many=True)
        return Response(serializer.data)


class booked_ticket_data(APIView):

    def get(self, request):
        booked_ticket = booked_tickets.objects.all()
        serializer = bookedticketSerializer(booked_ticket, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = bookedticketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class movie_update_data(APIView):

    def get(self,request):
        updates=movie_update.objects.all()
        serializer=updatemovieSerializer(updates,many=True)
        return Response(serializer.data)


class theatre_update_data(APIView):

    def get(self,request):
        updates=changes_on_theaters.objects.all()
        serializer=updatetheatreSerializer(updates,many=True)
        return Response(serializer.data)

class screen_update_data(APIView):

    def get(self,request):
        updates=changes_on_screens.objects.all()
        serializer=updatescreenSerializer(updates,many=True)
        return Response(serializer.data)

class ticket_update_data(APIView):

    def get(self,request):
        updates=ticket_update.objects.all()
        serializer=updateticketSerializer(updates,many=True)
        return Response(serializer.data)

