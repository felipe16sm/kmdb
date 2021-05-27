from kmdb_app.permissions import MoviePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.serializers import  MovieSerializer
from kmdb_app.models import Movie
import ipdb

class MovieView(GenericAPIView,
                                   ListModelMixin,
                                   CreateModelMixin,
                                   UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

