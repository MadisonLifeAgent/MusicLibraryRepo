from django.shortcuts import render
# imports Song model and songserializer - used for endpoint class-based view methods
from .models import Song
from .serializers import SongSerializer
# parent class for our class-based views - takes care of nuts and bolts of method routing/response to requestor
from rest_framework.views import APIView
# function call that converts our data into JSON string literal, and sends it to client requestion resources at specified endpoint
from rest_framework.response import Response
# enum (collection of values) the specify what status cude we would like to send back in response
from rest_framework import status


# Create your views here. - these handle requests made to our API
class SongList(APIView):

    # take in request parameter - which contains info about client's request
    # In APIs, requests can contain a lot of useful info (i.e. - parameters, headers, authentication tokens, and request type)
    def get(self, request):
        # query all the rows from our model table/db
        song = Song.objects.all()

        # pass the song query above into a new instantiation of our Serializer
        # many=True tells serializer that it is receiving a query set (object of many rows)
        # serializer takes all objects and convert them into Python native data type - in this case a list of dictionaries
        serializer = SongSerializer(song, many=True)

        # pass serializer.data (data property contains all model objects in a list of dictionaries) into Response object we are returning
        # response object converts list of dictionaries into a JSON string literal and returns it to requestor
        return Response(serializer.data)

    # endpoint allowing us to POST or create a new row in our database
    def post(self, request):
        # take data from body of request.data and pass into new instantiation of the serializer
        serializer = SongSerializer(data=request.data)

        # use is_valid() method to confirm the request's data contains all required fields present in our model definition
        if serializer.is_valid():
            # if True, JSON data from request's body will be converted into new model instance and saved to our table in db
            serializer.save()

            # returns serializer.data  and contet created message
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # return this if serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)