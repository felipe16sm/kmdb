from rest_framework import serializers
from . import GenreSerializer, ReviewSerializer, CommentSerializer

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
    criticism_set = ReviewSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)
