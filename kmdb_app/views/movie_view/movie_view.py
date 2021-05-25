from rest_framework.fields import DictField
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from kmdb_app.serializers import  CreateMovieSerializer, ReadMovieSerializer
from kmdb_app.models import Movie
from kmdb_app.services import MovieServices,GenreServices
import ipdb

class MovieView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Movie.objects.all()

    def post(self, request):
        serializer = CreateMovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        genres = data.pop('genres')

        movie = MovieServices.create_movie(data)

        for genre in genres:
            
            if not GenreServices.get_genre_by_name(genre['name']):
                genre = GenreServices.create_genre(genre)
            else:
                genre = GenreServices.get_genre_by_name(genre['name'])
            movie.genres.add(genre)

        

        # ipdb.set_trace()
        serializer = ReadMovieSerializer(movie)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
