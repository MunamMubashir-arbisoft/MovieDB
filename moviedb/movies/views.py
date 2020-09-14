from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Artist, Character
from .serializers import ArtistSerializer, MovieSerializer, CharacterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'


class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
