from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# get all songs or add a new song to db
class SongList(APIView):
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get song and update, edit, or delete song
class SongDetail(APIView):
    def get_by_id(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return HttpResponse(status=404)
        
    def get(self, request, pk):
        song = self.get_by_id(pk)
        serializer = SongSerializer(song)

        return Response(serializer.data)
        
    def put(self, request, pk):
        song = self.get_by_id(pk)
        serializer = SongSerializer(song, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    def delete(self, request, pk):
        song = self.get_by_id(pk)
        serializer = SongSerializer(song)

        song.delete()
        
        return Response(serializer.data, status=200)

# add likes to song
class Likes(APIView):
    def get_by_id(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            return HttpResponse(status=404)

    def put(self, request, pk):
        song = self.get_by_id(pk)

        current_likes = song.likes

        serializer = SongSerializer(song, data=request.data)

        if serializer.is_valid():
            serializer.validated_data['likes'] = current_likes + serializer.validated_data['likes']

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)