from django.db import models
from django.utils.text import slugify
from django.core.files import File

from urllib.request import urlopen

from tempfile import NamedTemporaryFile


GENRE_CHOICES = (
    ('action', 'Action'),
    ('adventure', 'Adventure'),
    ('animation', 'Animation'),
    ('comedy', 'Comedy'),
    ('crime', 'Crime'),
    ('drama', 'Drama'),
    ('history', 'History'),
    ('romance', 'Romance'),
    ('sci-fi', 'Sci-fi'),
    ('war', 'War'),
)

LANGUAGE_CHOICES = (
    ('english', 'English'),
    ('french', 'French'),
    ('german', 'German'),
    ('spanish', 'Spanish'),
    ('hindi', 'Hindi'),
    ('tamil', 'Tamil'),
)


class DirectorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(directed_movies__isnull=True)


class ActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(character_played__isnull=True)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.CharField(max_length=300)
    directors = DirectorManager()
    actors = ActorManager()
    objects = models.Manager()

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=150)
    actor = models.ForeignKey('movies.Artist',
                              related_name='character_played',
                              on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie',
                              related_name='characters',
                              on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(choices=GENRE_CHOICES, max_length=50)
    objects = models.Manager()

    def save(self, *args, **kwargs):
        if Genre.objects.filter(name__iexact=self.name).exists():
            return
        self.name = self.name.lower()
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200,
                            unique=True)
    release_date = models.DateField()
    plot = models.TextField(max_length=500)
    runtime = models.IntegerField()
    poster_image = models.ImageField(upload_to="movie-poster/", blank=True, null=True)
    poster_image_url = models.URLField(blank=True, null=True)
    genre = models.ForeignKey('movies.Genre',
                              related_name='movies',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    director = models.ManyToManyField('movies.Artist',
                                      related_name='directed_movies',
                                      editable=True,
                                      blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                max_length=50)
    objects = models.Manager()

    def get_all_actors(self):
        actors = [character.actor for character in self.characters.all()]
        return actors

    def __str__(self):
        return self.title

    def create(self, validated_data):
        genre_validated_data = validated_data.pop('genre')
        genre = Genre.objects.create(**genre_validated_data)
        movie = Movie.objects.create(genre=genre, **validated_data)
        return movie

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre')
        instance = super().update(instance, validated_data)
        instance.genre = genre
        instance.save()
        return instance

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Movie, self).save(*args, **kwargs)

        if self.poster_image_url and not self.poster_image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.poster_image_url).read())
            img_temp.flush()
            self.poster_image.save(f"image_{self.pk}_{self.slug}", File(img_temp))

