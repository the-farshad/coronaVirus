from django.db import models
from django.urls import reverse


# Create your models here.
class Countries(models.Model):
    country = models.CharField(max_length=50, default='')
    countryKurdishName = models.CharField(max_length=50, default='')
    _id = models.IntegerField(default=0)
    ios2 = models.CharField(max_length=2, default='')
    ios3 = models.CharField(max_length=3, default='')
    latitude = models.DecimalField(max_digits=12, decimal_places=10)
    longitude = models.DecimalField(max_digits=12, decimal_places=10)
    cases = models.IntegerField(default=0)
    todayCases = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    todayDeaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
    critical = models.IntegerField(default=0)
    casesPerOneMillion = models.IntegerField(default=0)
    deathsPerOneMillion = models.IntegerField(default=0)
    bearing = models.DecimalField(max_digits=4, decimal_places=2)
    zoom = models.DecimalField(max_digits=4, decimal_places=2)
    priority = models.IntegerField()
