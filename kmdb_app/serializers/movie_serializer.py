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
