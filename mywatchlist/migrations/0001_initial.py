# Generated by Django 4.1 on 2022-09-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchlistItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_watched', models.TextField()),
                ('movie_title', models.TextField()),
                ('movie_rating', models.IntegerField()),
                ('movie_release_date', models.TextField()),
                ('movie_review', models.TextField()),
            ],
        ),
    ]
