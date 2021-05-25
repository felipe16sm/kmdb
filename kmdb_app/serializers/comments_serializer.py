from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    commment = serializers.CharField()
