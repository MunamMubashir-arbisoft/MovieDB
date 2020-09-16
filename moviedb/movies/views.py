from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Movie, Artist, Character
from .serializers import ArtistSerializer, MovieSerializer, CharacterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ('title', 'characters__name', 'director__name', 'genre__name',)
    filter_backends = (filters.SearchFilter,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'


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

