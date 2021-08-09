from rest_framework import serializers
from .models import Song

# serializer for converting JSON content to and from python class objects
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'likes']
