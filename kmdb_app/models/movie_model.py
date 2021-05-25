from django.db import models
from kmdb_app.models import Genre

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    launch = models.CharField(max_length=255)
    classification = models.IntegerField()
    synopsis = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
