from django.db import models
from kmdb_app.models import Movie, User

class Criticism(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
