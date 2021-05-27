from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from kmdb_app.permissions import ReviewPermission
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from kmdb_app.serializers import  CriticismSerializer
from kmdb_app.models import  Criticism
from kmdb_app.services import MovieServices, CriticismServices
import ipdb

class ReviewView(GenericAPIView,
                                   CreateModelMixin,
                                   UpdateModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermission]
    queryset = Criticism.objects.all()
    serializer_class = CriticismSerializer

    def create(self, request, *args, **kwargs):
        movie = MovieServices.get_movie(int(kwargs['movie_id']))
        criticism = CriticismServices.create_criticism(request.data, movie, request.user)

        if criticism == '422':
            return Response({'detail': 'You already made this review.'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if criticism == '400':
            return Response({'detail': 'You already made this review.'},status=status.HTTP_400_BAD_REQUEST)

        return Response(CriticismSerializer(criticism).data, status=status.HTTP_201_CREATED)
        

    def partial_update(self, request, *args, **kwargs):
        movie = MovieServices.get_movie(int(kwargs['movie_id']))

        criticism = CriticismServices.update_criticism(request.data, request.user, movie)

        if criticism == '404':
            return Response({"error":"Review not founded"}, status=status.HTTP_404_NOT_FOUND)

        return Response(CriticismSerializer(criticism).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

