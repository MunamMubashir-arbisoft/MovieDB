from rest_framework import serializers
from .models import Movie, Artist, Character


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'date_of_birth', 'bio']


class CharacterSerializer(serializers.ModelSerializer):
    actor = ArtistSerializer()
    movie = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Character
        fields = ['name', 'actor', 'movie']

    def __init__(self, *args, **kwargs):
        super(CharacterSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['POST', 'PUT']:
                self.fields['actor'] = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
                self.fields['movie'] = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
        except KeyError:
            pass


class MovieSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    poster_image = serializers.ImageField(required=False, allow_null=True)
    slug = serializers.SlugField(read_only=True)
    director = ArtistSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['slug', 'title', 'plot', 'release_date', 'runtime', 'poster_image',
                  'language', 'genre', 'director', 'characters']

    def __init__(self, *args, **kwargs):
        super(MovieSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['POST', 'PUT']:
                self.fields['director'] = serializers.PrimaryKeyRelatedField(many=True,
                                                                             queryset=Artist.objects.all())
        except KeyError:
            pass
