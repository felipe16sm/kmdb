from rest_framework import serializers
from . import ShowUserSerializer
from kmdb_app.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = ShowUserSerializer(read_only=True)
    comment = serializers.CharField()
    
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment']
