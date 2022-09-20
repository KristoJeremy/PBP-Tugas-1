from django.db import models

class WatchlistItems(models.Model):
    movie_watched = models.TextField()
    movie_title = models.TextField()
    movie_rating = models.IntegerField()
    movie_release_date = models.TextField()
    movie_review = models.TextField()