from rest_framework import serializers
from kmdb_app.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name']
