from django.db import models

from datetime import datetime

# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    age= models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Song (models.Model):
    #Artiste = models.ForeignKey(Artiste, on_delete= models.CASCADE)
    title = models.CharField(max_length=80)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric (models.Model):
    #Song = models.ForeignKey(Song, on_delete= models.CASCADE)
    content = models.CharField(max_length= 500)
    song_id = models.IntegerField()

    def __str__(self):
        return self.content

