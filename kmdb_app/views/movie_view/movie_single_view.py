from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.serializers import  MovieSerializer
from kmdb_app.permissions import MoviePermission
from kmdb_app.models import Movie
from kmdb_app.services import MovieServices
import ipdb

class MovieSingleView(GenericAPIView,
                                   ListModelMixin,
                                   UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):        
        movie = MovieServices.get_movie(int(kwargs['movie_id']))
        return Response(MovieSerializer(movie).data,status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        MovieServices.delete_movie(int(kwargs['movie_id']))
        return Response(status=status.HTTP_204_NO_CONTENT)
