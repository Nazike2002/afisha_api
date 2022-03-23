from rest_framework import serializers
from .models import *

# class DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Director
#         fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name count_movies'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews rating'.split()

class DirectorСreqteUpdateSrializer(serializers.Serializer):
    name = serializers.CharField()

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.TimeField()
    director = serializers.IntegerField()

class ReviewCreateUpdateSerialiser(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField(default=5)

