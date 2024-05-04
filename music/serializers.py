from rest_framework import serializers
from .models import Artist,Albom,Songs

class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ("name","image")


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Albom
        fields = ("__all__")

class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)
    class Meta:
        model = Songs
        fields = ("__all__")