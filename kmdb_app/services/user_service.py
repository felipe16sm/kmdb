from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from kmdb_app.models import User

class UserServices():
    @staticmethod
    def create_user(user_data, password):
        return User.objects.create_user(**user_data,password=password)

    @staticmethod
    def find_user_by_username(username):
        return User.objects.filter(username=username).first()

    @staticmethod
    def authenticate_user(username, password):
        return authenticate(
            username=username, password=password)
    
    @staticmethod
    def create_token(user):
        return Token.objects.get_or_create(user=user)[0]


    
