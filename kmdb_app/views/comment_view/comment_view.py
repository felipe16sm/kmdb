from kmdb_app import serializers
from kmdb_app.services.comment_service import CommentServices
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from kmdb_app.permissions import CreateCommentPermission
from kmdb_app.serializers import  CommentSerializer, UpdateCommentSerializer
from kmdb_app.models import Comment, Movie
from kmdb_app.services import MovieServices
import ipdb

class CommentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CreateCommentPermission]
    queryset = Comment.objects.all()

    def post(self, request, movie_id):
        movie = MovieServices.get_movie(movie_id)

        serializer = CommentSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        
        comment = CommentServices.create_comment(serializer.data, movie, request.user)

        serializer = CommentSerializer(comment)

        return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        

    def put(self, request, movie_id):
        movie = MovieServices.get_movie(movie_id)

        comment = CommentServices.get_comment_by_id(request.data['comment_id'])

        serializer = UpdateCommentSerializer(data = request.data)
        
        if not serializer.is_valid():
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        
        comment = CommentServices.update_comment(serializer.data)
        
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
