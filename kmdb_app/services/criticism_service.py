from django.shortcuts import get_object_or_404
from kmdb_app.models import Movie, Criticism
import ipdb

class CriticismServices():
    @staticmethod
    def get_criticism_by_id(criticism_id):
        return get_object_or_404(Criticism, id=criticism_id)

    @staticmethod
    def get_criticism_by_critic(critic):
        return Criticism.objects.filter(critic=critic)

    @staticmethod
    def get_criticism_by_critic_and_movie(critic, movie):
        return Criticism.objects.filter(critic=critic, movie=movie).first()

    @staticmethod
    def get_criticism_by_movie(movie):
        criticism = Criticism.objects.filter(movie=movie)
        return criticism

    @staticmethod
    def update_criticism(criticism_data, critic, movie):
        
        criticism = CriticismServices.get_criticism_by_critic_and_movie(critic, movie)
        
        if not criticism:
            return '404'

        criticism.stars = criticism_data['stars']
        criticism.review = criticism_data['review']
        criticism.spoilers = criticism_data['spoilers']
        criticism.save()
        return criticism


    @staticmethod
    def create_criticism(criticism_data, movie, critic):
        if not (criticism_data['stars']>=1 and criticism_data['stars']<=10):
            return '400'
        
        if len(CriticismServices.get_criticism_by_critic(critic)) == 0:
            return Criticism.objects.create(**criticism_data, movie=movie, critic=critic)
        
        return '422'
