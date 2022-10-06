from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMovie
        fields = '__all__'

    movie = MovieSerializer()
    person = PersonSerializer()


class PersonMovieSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = PersonMovie
        fields = '__all__'


class DirectorMovieSerializer(serializers.ModelSerializer):

    director = serializers.StringRelatedField(source='personmovie_set', many=True, read_only=True)
    persons = serializers.SlugRelatedField(source='personmovie_set', many=True, read_only=True, slug_field='person_id')
    position = serializers.SlugRelatedField(source='personmovie_set', many=True, read_only=True, slug_field='category')
    role = serializers.SlugRelatedField(source='personmovie_set', many=True, read_only=True, slug_field='characters')

    class Meta:
        model = Movie
        fields = ['id', 'imdb_id', 'name', 'year', 'genres', 'director', 'persons', 'position', 'role']
