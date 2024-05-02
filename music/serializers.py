
from rest_framework import serializers
from .models import Artist, Album, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", 'name', 'image', 'last_updated')


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ("id", 'title', 'artist', 'cover', 'last_updated')


class SongsSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = ("id", 'title', 'cover', 'album', 'last_updated')



