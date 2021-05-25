from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from kmdb_app.serializers import  ReadMovieSerializer
from kmdb_app.permissions import MoviePermission
from kmdb_app.models import Movie
from kmdb_app.services import MovieServices
import ipdb

class MovieSingleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MoviePermission]
    queryset = Movie.objects.all()

    def get(self, request, movie_id):
        movie = MovieServices.get_movie(movie_id)
        
        return Response(ReadMovieSerializer(movie).data,status=status.HTTP_200_OK)

    def delete(self, request, movie_id):
        movie = MovieServices.delete_movie(movie_id)
            
        return Response("", status=status.HTTP_204_NO_CONTENT)
