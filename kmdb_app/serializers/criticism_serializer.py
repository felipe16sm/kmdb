from rest_framework import serializers
from .user_serializer import ShowUserSerializer

class CriticismSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    critic = ShowUserSerializer(read_only=True)
    stars = serializers.IntegerField()
    review = serializers.CharField()
    spoilers = serializers.BooleanField()
