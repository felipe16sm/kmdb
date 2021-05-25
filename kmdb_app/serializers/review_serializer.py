from rest_framework import serializers

class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    review = serializers.CharField()