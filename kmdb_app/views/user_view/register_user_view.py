from kmdb_app.models.user_model import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.serializers import UserSerializer
from kmdb_app.services import UserServices
import ipdb

class RegisterUserView(GenericAPIView,
                                   ListModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = UserServices.find_user_by_username(request.data['username'])
        if user:
            return Response({'username': ['A user with that username already exists.']}, status=status.HTTP_400_BAD_REQUEST)
        
        password = request.data.pop('password')
        
        user = UserServices.create_user(request.data, password)

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)
