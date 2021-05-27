import ipdb
from rest_framework import serializers
from . import GenreSerializer, CriticismSerializer, CommentSerializer
from kmdb_app.services import MovieServices, GenreServices
from kmdb_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    genres = GenreSerializer(many=True)
    criticism_set = CriticismSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'launch', 'classification', 'synopsis', 'genres', 'criticism_set', 'comment_set']
    
    def create(self, data):
        genres = data.pop('genres')
        movie = MovieServices.create_movie(data)

        for genre in genres:
            if not GenreServices.get_genre_by_name(genre['name']):
                genre = GenreServices.create_genre(genre)
            else:
                genre = GenreServices.get_genre_by_name(genre['name'])
            movie.genres.add(genre)
        
        return movie



class CreateMovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    duration = serializers.CharField()
    genres = GenreSerializer(many=True)
    launch = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

class ReadMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    duration = serializers.CharField(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)
    launch = serializers.CharField(read_only=True)
    classification = serializers.IntegerField(read_only=True)
    synopsis = serializers.CharField(read_only=True)
    criticism_set = CriticismSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)
