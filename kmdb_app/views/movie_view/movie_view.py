from kmdb_app.permissions import MoviePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from kmdb_app.serializers import  MovieSerializer
from kmdb_app.models import Movie
import ipdb

class ListMovieMixin(object):
    def list(self, request, *args, **kwargs):
        objects = self.queryset.all()
        if len(request.data) > 0:
            objects = self.model.objects.filter(title__icontains=request.data['title'])
        return Response([self.serializer_class(obj).data for obj in objects], status=status.HTTP_200_OK)
        


class MovieView(GenericAPIView,
                                   ListMovieMixin,
                                   CreateModelMixin,  
                                   ):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

