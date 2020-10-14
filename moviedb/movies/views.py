from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Movie, Artist, Character
from .serializers import ArtistSerializer, MovieSerializer, CharacterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('title', 'characters__name', 'director__name', 'genre__name',)
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('name',)
    filter_backends = (filters.SearchFilter,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('name', 'actor__name',)
    filter_backends = (filters.SearchFilter,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class MovieCharactersAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CharacterSerializer

    def get(self, request, movie_id, format=None):
        characters_for_movie = Character.objects.filter(movie__id=movie_id).distinct()
        serializer = self.serializer_class(characters_for_movie, many=True)
        return Response(serializer.data)

