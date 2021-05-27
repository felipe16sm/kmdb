from rest_framework import serializers
from . import ShowUserSerializer

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = ShowUserSerializer(read_only=True)
    comment = serializers.CharField()
    
    class Meta:
        fields=['id', 'user', 'comment']
