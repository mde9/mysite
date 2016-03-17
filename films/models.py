from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Film(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class CSchedue(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    film_date = models.DateTimeField('film date')
    reserved_places = models.IntegerField(default=0)
    places = models.IntegerField(default=150)

    def __str__(self):
        return self.film_date.strftime("%Y-%m-%d %H:%M")+ ",  free places:"+str(self.places-self.reserved_places) 
    def is_avaiable_places(self):
        return self.reserved_places<self.places
# Create your models here.

