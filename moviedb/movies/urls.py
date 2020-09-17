from rest_framework import routers
from django.urls import path

from .views import MovieViewSet, ArtistViewSet, CharacterViewSet, MovieCharactersAPIView


app_name = "movies"
router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'characters', CharacterViewSet)

urlpatterns = [
    path('characters/movie=<int:movie_id>/', MovieCharactersAPIView.as_view(), name='movie_characters')
]

urlpatterns += router.urls
