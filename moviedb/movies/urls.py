from rest_framework import routers

from .views import MovieViewSet, ArtistViewSet, CharacterViewSet


app_name = "movies"
router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'characters', CharacterViewSet)
urlpatterns = router.urls
