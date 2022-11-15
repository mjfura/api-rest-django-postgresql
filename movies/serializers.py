from rest_framework import serializers
from movies import models

class PosterArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PosterArt
        fields=["id","url","width","height"]
        read_only_fields=("id",)

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ImageList
        fields=["id","posterArt"]
        read_only_fields=("id",)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields=("title","description","releaseYear","id","images")
        read_only_fields=("id",)
        
    