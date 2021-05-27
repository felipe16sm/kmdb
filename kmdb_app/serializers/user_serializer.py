from rest_framework import serializers
from kmdb_app.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff']

class ShowUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class CredentialSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']
