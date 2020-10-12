from rest_framework import serializers
from .models import Movie, Artist, Character, Genre


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'date_of_birth', 'bio']


class CharacterSerializer(serializers.ModelSerializer):
    actor = ArtistSerializer()
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True)

    class Meta:
        model = Character
        fields = ['id', 'name', 'actor', 'movie']

    def __init__(self, *args, **kwargs):
        super(CharacterSerializer, self).__init__(*args,
                                                  **kwargs)
        try:
            if self.context['request'].method in ['POST', 'PUT']:
                self.fields['actor'] = serializers.PrimaryKeyRelatedField(
                    queryset=Artist.objects.all()
                )
        except KeyError:
            pass


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True,
                                     read_only=True)
    poster_image_url = serializers.URLField(required=False,
                                            allow_null=True)
    slug = serializers.SlugField(read_only=True)
    director = ArtistSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'slug', 'title', 'plot', 'release_date', 'runtime', 'poster_image_url',
                  'language', 'genre', 'director', 'characters']

    def __init__(self, *args, **kwargs):
        super(MovieSerializer, self).__init__(*args,
                                              **kwargs)
        try:
            if self.context['request'].method in ['POST', 'PUT']:
                self.fields['director'] = serializers.PrimaryKeyRelatedField(
                    many=True,
                    queryset=Artist.objects.all()
                )
        except KeyError:
            pass

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        director_data = validated_data.pop('director')
        genre, _ = Genre.objects.get_or_create(**genre_data)
        instance = Movie.objects.create(genre=genre,
                                        **validated_data)
        instance.director.set(director_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre')
        genre, _ = Genre.objects.get_or_create(**genre_data)
        director_data = validated_data.pop('director')
        instance = super().update(instance,
                                  validated_data)
        instance.director.set(director_data)
        instance.genre = genre
        instance.save()
        return instance
