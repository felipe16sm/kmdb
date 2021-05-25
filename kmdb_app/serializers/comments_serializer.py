from rest_framework import serializers
from . import ShowUserSerializer

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = ShowUserSerializer(read_only=True)
    comment = serializers.CharField()

class UpdateCommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    comment = serializers.CharField()
