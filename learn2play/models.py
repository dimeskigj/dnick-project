from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return f"title: {self.title} artist: {self.artist} text: {self.text}"
