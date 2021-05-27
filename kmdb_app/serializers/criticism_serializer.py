import ipdb
from rest_framework import serializers
from .user_serializer import ShowUserSerializer
from kmdb_app.models import Criticism
from kmdb_app.services import CriticismServices, MovieServices

class CriticismSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    critic = ShowUserSerializer(read_only=True)
    
    class Meta:
        model = Criticism
        fields = ['id', 'critic', 'stars', 'review', 'spoilers']
    

