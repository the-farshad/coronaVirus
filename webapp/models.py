from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Country(models.Model):
    country = models.CharField(
        max_length=50,
        default='',
        verbose_name='Country Name'
    )
    countryKurdishName = models.CharField(
        max_length=50,
        default='',
        verbose_name='Kurdish Name'
    )
    _id = models.PositiveSmallIntegerField(default=0)
    iso2 = models.CharField(max_length=2, default='')
    iso3 = models.CharField(max_length=3, default='')
    latitude = models.DecimalField(max_digits=14, decimal_places=10)
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=14, decimal_places=10)
    long = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    cases = models.PositiveIntegerField(default=0)
    todayCases = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    todayDeaths = models.PositiveIntegerField(default=0)
    recovered = models.PositiveIntegerField(default=0)
    active = models.PositiveIntegerField(default=0)
    critical = models.PositiveIntegerField(default=0)
    tests = models.PositiveIntegerField(default=0)
    casesPerOneMillion = models.PositiveIntegerField(default=0)
    deathsPerOneMillion = models.PositiveIntegerField(default=0)
    bearing = models.DecimalField(max_digits=4, decimal_places=2)
    zoom = models.DecimalField(max_digits=4, decimal_places=2)
    priority = models.SmallIntegerField()
    flag = models.URLField(max_length=200, default='')
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    continent = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return f'{self.iso3} --> {self.country}'

    class Meta:
        verbose_name = 'Country List'
        verbose_name_plural = 'Countries List'
        ordering = ['priority']
        indexes = [
            models.Index(fields=['country'], name='country')
        ]
