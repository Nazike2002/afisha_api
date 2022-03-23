from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from main.models import Director, Movie, Review
from main.serializers import DirectorSerializer, MovieCreateUpdateSerializer, MovieSerializer, ReviewCreateUpdateSerialiser, ReviewSerializer, DirectorСreqteUpdateSrializer


@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = DirectorСreqteUpdateSrializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        Director.objects.create(name=name)
        return Response(data={'message': 'Date Reseived!'})


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        DTDirector = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data='DirectorNotFound')
    if request.method == 'GET':
        data = DirectorSerializer(DTDirector).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTDirector.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = DirectorСreqteUpdateSrializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTDirector.name = request.data.get('name')
        DTDirector.save()
        return Response(data=DirectorSerializer(DTDirector).data)




@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data =  MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = MovieCreateUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors':serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        Movie.objects.create(title=title, description=description, duration=duration, director=director)
        return Response(data={'message': 'Date Reseived!'})
# {
#     "title": "Marvel",
#     "description": "XXA",
#     "duration": "05:54:15",
#     "director": 2
# }

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        DTMovie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data='MovieNotFound')
    if request.method == 'GET':
        data = MovieSerializer(DTMovie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTMovie.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = MovieCreateUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTMovie.title = request.data.get('title')
        DTMovie.description = request.data.get('description')
        DTMovie.duration = request.data.get('duration')
        DTMovie.director = request.data.get('director')
        DTMovie.save()
        return Response(data=MovieSerializer(DTMovie).data)



@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        movie = Review.objects.all()
        data = ReviewSerializer(movie, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = ReviewCreateUpdateSerialiser(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        Review.objects.create(text=text,movie=movie,stars=stars)
        return Response(data={'message': 'Date Reseived!'})


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        DTReview = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data='ReviewNotFound')
    if request.method == 'GET':
        data = ReviewSerializer(DTReview).data
        return Response(data=data)
    elif request.method == 'DELETE':
        DTReview.delete()
        return Response('no content')
    elif request.method == 'PUT':
        serializers = ReviewCreateUpdateSerialiser(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        DTReview.text = request.data.get('text')
        DTReview.movie = request.data.get('movie')
        DTReview.stars = request.data.get('stars')
        DTReview.save()
        return Response(data=ReviewSerializer(DTReview).data)