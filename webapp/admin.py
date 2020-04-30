from django.contrib import admin
from django.conf import settings
from .models import Country


# Register your models here.
class CountryStatistic(admin.ModelAdmin):
    search_fields = ['country', 'countryKurdishName', 'iso3']
    list_display = ['country', 'countryKurdishName', 'iso3', 'updated']


if settings.DEBUG:
    admin.site.register(Country,  CountryStatistic)
