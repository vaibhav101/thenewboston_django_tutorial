from django.db import models


class Album(models.Model):
    def __str__(self):
        return "%s - %s" % (self.artist, self.album_title)

    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=1000)


class Song(models.Model):
    def __str__(self):
        return "%s - %s" % (self.album, self.song_title)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)
