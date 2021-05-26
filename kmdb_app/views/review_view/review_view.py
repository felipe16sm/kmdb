from kmdb_app import serializers
from kmdb_app.services.comment_service import CommentServices
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from kmdb_app.permissions import ReviewPermission
from kmdb_app.serializers import  CriticismSerializer
from kmdb_app.models import  Movie, Criticism
from kmdb_app.services import MovieServices, CriticismServices
import ipdb

class ReviewView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermission]
    queryset = Criticism.objects.all()

    def post(self, request, movie_id):
        movie = MovieServices.get_movie(movie_id)

        serializer = CriticismSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

        criticism = CriticismServices.create_criticism(serializer.data, movie, request.user)

        if criticism == '422':
            return Response({'detail': 'You already made this review.'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if criticism == '400':
            return Response({'detail': 'You already made this review.'},status=status.HTTP_400_BAD_REQUEST)


        serializer = CriticismSerializer(criticism)

        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        

    def put(self, request, movie_id):
        movie = MovieServices.get_movie(movie_id)

        if not movie:
            Response({"error":"Movie not founded"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CriticismSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        
        criticism = CriticismServices.update_criticism(serializer.data, request.user, movie)
        
        if criticism == '404':
            return Response({"error":"Review not founded"}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = CriticismSerializer(criticism)

        return Response(serializer.data, status=status.HTTP_200_OK)
