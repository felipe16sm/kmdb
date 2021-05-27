from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.serializers import CredentialSerializer
from kmdb_app.services import UserServices
from kmdb_app.models import User

class LoginView(GenericAPIView,
                                   ListModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = CredentialSerializer

    def create(self, request, *args, **kwargs):
        
        user = UserServices.authenticate_user(request.data['username'], request.data['password'])

        if user:
            token = UserServices.create_token(user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)
