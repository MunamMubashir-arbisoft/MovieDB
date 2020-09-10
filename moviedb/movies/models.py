from django.db import models
from django.utils.text import slugify


GENRE_CHOICES = (
    ('action', 'ACTION'),
    ('adventure', 'ADVENTURE'),
    ('animation', 'ANIMATION'),
    ('comedy', 'COMEDY'),
    ('drama', 'DRAMA'),
    ('romance', 'ROMANCE'),
)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.CharField(max_length=300)


class Character(models.Model):
    name = models.CharField(max_length=150)
    actor = models.ForeignKey('movies.Artist',
                              related_name='character_played',
                              on_delete=models.CASCADE)
    movie = models.OneToOneField('movies.Movie',
                                 related_name='characters',
                                 on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    release_date = models.DateField()
    plot = models.TextField(max_length=500)
    runtime = models.IntegerField()
    poster_image = models.ImageField()
    genre = models.CharField(choices=GENRE_CHOICES,
                             max_length=30)
    director = models.ManyToManyField('movies.Artist',
                                      related_name='directed_movies',
                                      blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)