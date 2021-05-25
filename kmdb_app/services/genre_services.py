from django.shortcuts import get_object_or_404
from kmdb_app.models import Genre

class GenreServices():
    @staticmethod
    def create_genre(genre_data):
        return Genre.objects.create(**genre_data)

    @staticmethod
    def get_genre_by_name(genre_name):
        return Genre.objects.filter(name=genre_name).first()
    
    @staticmethod
    def list_all_genres():
        return Genre.objects.all()


    
