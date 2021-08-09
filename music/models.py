from django.db import models

# Create your models here.

# Song model/class
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField(null=True, editable=True, blank=True)
    likes = models.IntegerField(null=True, default='0', blank=True)