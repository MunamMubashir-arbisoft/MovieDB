from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):
    user = models.ManyToManyField('users.Account',
                                  related_name='notifications',
                                  editable=True)
    message = models.TextField()
    movie = models.ForeignKey('movies.Movie',
                              related_name='notifications',
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


@receiver(post_save, sender='movies.Movie')
def create_notification(sender, instance, created, **kwargs):
    users_following_movie = instance.genre.users_following.all()

    for director in instance.director.all():
        director.users_following.all()
        users_following_movie = (users_following_movie | director.users_following.all())

    for actor in instance.get_all_actors():
        users_following_movie = (users_following_movie | actor.users_following.all())

    for user in users_following_movie.distinct():
        notification, _ = Notification.objects.get_or_create(
            message="New movie, {}, has been added.".format(instance.title),
            movie=instance
        )
        notification.user.add(user)
