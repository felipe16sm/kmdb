from django.db import models
from kmdb_app.models import Movie, User

class Review(models.Model):
    review = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
