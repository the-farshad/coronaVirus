# -*- codeing: utf-8 -*-

from json import JSONEncoder

from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from .models import Country
from getdata import main


# Create your views here.
def countries_view(request):
    # list of countries show in page
    queryset = Country.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, 'home.html', context)


def database_update(request, *args, **kwargs):
    data_gathered = main()
    Country.objects.all().delete()
    for data in data_gathered:
        if data_gathered[data]['_id'] is not None:
            Country.objects.create(
                country=data,
                countryKurdishName=data_gathered[data]['countryKurdishName'],
                cases=data_gathered[data]['cases'],
                todayCases=data_gathered[data]['todayCases'],
                deaths=data_gathered[data]['deaths'],
                todayDeaths=data_gathered[data]['todayDeaths'],
                recovered=data_gathered[data]['recovered'],
                critical=data_gathered[data]['critical'],
                active=data_gathered[data]['active'],
                latitude=data_gathered[data]['latitude'],
                longitude=data_gathered[data]['longitude'],
                bearing=data_gathered[data]['bearing'],
                zoom=data_gathered[data]['zoom'],
                priority=data_gathered[data]['priority'],
                flag=data_gathered[data]['flag'],
                _id=data_gathered[data]['_id'],
                iso2=data_gathered[data]['iso2'],
                iso3=data_gathered[data]['iso3'],
                updated=data_gathered[data]['updated'],
                continent=data_gathered[data]['continent']
            )
    return JsonResponse(data_gathered, JSONEncoder)


def handler404(request, *args, **kwargs):
    return redirect('/')
