from django.db import models
from django.urls import reverse

class Album(models.Model):
    def __str__(self):
        return "%s - %s" % (self.artist, self.album_title)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={"pk": self.pk,})

    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_logo = models.FileField()


class Song(models.Model):
    def __str__(self):
        return "%s - %s" % (self.album, self.song_title)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)
