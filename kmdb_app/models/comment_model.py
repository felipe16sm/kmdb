from django.db import models
from kmdb_app.models import Movie, User

class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
