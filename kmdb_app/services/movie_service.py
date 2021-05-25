from django.shortcuts import get_object_or_404
from kmdb_app.models import Movie

class MovieServices():
    @staticmethod
    def create_movie(movie_data):
        return Movie.objects.create(**movie_data)

    @staticmethod
    def get_movie(movie_id):
        return get_object_or_404(Movie, id=movie_id)

    @staticmethod
    def delete_movie(movie_id):
        movie = MovieServices.get_movie(movie_id)
        return movie.delete()
    
    @staticmethod
    def list_all_movies():
        return Movie.objects.all()


    
