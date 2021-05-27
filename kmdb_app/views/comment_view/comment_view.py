from kmdb_app import serializers
from kmdb_app.services.comment_service import CommentServices
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.permissions import CommentPermission
from kmdb_app.serializers import  CommentSerializer
from kmdb_app.models import Comment
from kmdb_app.services import MovieServices
import ipdb

class CommentView(GenericAPIView,
                                   ListModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CommentPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def create(self, request, *args, **kwargs):
        movie = MovieServices.get_movie(int(kwargs['movie_id']))

        comment = CommentServices.create_comment(request.data, movie, request.user)

        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        movie = MovieServices.get_movie(int(kwargs['movie_id']))

        comment = CommentServices.get_comment_by_id(int(kwargs['movie_id']))

        comment = CommentServices.update_comment(request.data, request.data['comment_id'])

        return Response(CommentSerializer(comment).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

