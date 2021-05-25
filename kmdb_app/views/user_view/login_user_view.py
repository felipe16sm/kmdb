from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from kmdb_app.serializers import CredentialSerializer
from kmdb_app.services import UserServices

class LoginView(APIView):
    def post(self, request):
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = UserServices.authenticate_user(request.data['username'], request.data['password'])

        if user:
            token = UserServices.create_token(user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
