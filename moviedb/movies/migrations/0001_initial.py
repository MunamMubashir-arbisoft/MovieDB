# Generated by Django 3.1.1 on 2020-09-10 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('bio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200)),
                ('release_date', models.DateField()),
                ('plot', models.TextField(max_length=500)),
                ('runtime', models.IntegerField()),
                ('poster_image', models.ImageField(upload_to='')),
                ('genre', models.CharField(choices=[('action', 'ACTION'), ('adventure', 'ADVENTURE'), ('animation', 'ANIMATION'), ('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=30)),
                ('language', models.CharField(max_length=50)),
                ('director', models.ManyToManyField(blank=True, related_name='directed_movies', to='movies.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='character_played', to='movies.artist')),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='movies.movie')),
            ],
        ),
    ]