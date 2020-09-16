from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    username = models.CharField(max_length=50,
                                unique=True)
    followed_genres = models.ManyToManyField('movies.Genre',
                                             related_name='users_following',
                                             blank=True)
    followed_artists = models.ManyToManyField('movies.Artist',
                                              related_name='users_following',
                                              blank=True)

    def __str__(self):
        return self.username
