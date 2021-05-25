from kmdb_app.models.user_model import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from kmdb_app.serializers import UserSerializer
from kmdb_app.services import UserServices
import ipdb

class RegisterUserView(APIView):
    def post(self, request):
        user = UserServices.find_user_by_username(request.data['username'])
        
        if user:
            return Response({"error":"Este usuário já existe"}, status=status.HTTP_409_CONFLICT)

        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = UserServices.create_user(serializer.data, request.data['password'])

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
