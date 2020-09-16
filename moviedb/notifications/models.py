from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):
    users = models.ManyToManyField('users.Account', related_name='notifications', blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def add_users(self, movie):
        users_following_artists = []
        users_following_genre = list(movie.genre.users_following.all())
        [users_following_artists.extend(list(director.users_following.all())) for director in movie.director.all()]
        [users_following_artists.extend(list(actor.users_following.all())) for actor in movie.get_all_actors()]
        total_user_following = users_following_artists + users_following_genre
        self.users.set(total_user_following)
        self.save()


@receiver(post_save, sender='movies.Movie')
def create_notification(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
            message="New movie,  {}, added that you might be interested in".format(instance.title))

        notification.add_users(instance)
