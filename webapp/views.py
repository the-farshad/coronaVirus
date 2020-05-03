# -*- codeing: utf-8 -*-

from json import JSONEncoder
from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Country
from getdata import main
from . import serializers


data_gathered = {
    'Af': {
        'country': 'Afghanistan',
        'countryKurdishName': 'ئەفغانستان',
        '_id': 4,
        'iso2': 'AF',
        'iso3': 'AFG',
        'latitude': '33.9391100000',
        'lat': '33.000000',
        'longitude': '67.7099530000',
        'long': '65.000000',
        'cases': 2704,
        'todayCases': 235,
        'deaths': 85,
        'todayDeaths': 13,
        'recovered': 345,
        'active': 2274,
        'critical': 7,
        'tests': 11068,
        'casesPerOneMillion': 69,
        'deathsPerOneMillion': 2,
        'bearing': '0.50',
        'zoom': '3.00',
        'priority': 16,
        'flag': 'https://corona.lmao.ninja/assets/img/flags/af.png',
        'continent': 'Asia'
    },
    'Af2': {
        'country': 'Afghanistan',
        'countryKurdishName': 'ئەفغانستان',
        '_id': 4,
        'iso2': 'AF',
        'iso3': 'AFG',
        'latitude': '33.9391100000',
        'lat': '33.000000',
        'longitude': '67.7099530000',
        'long': '65.000000',
        'cases': 2704,
        'todayCases': 235,
        'deaths': 85,
        'todayDeaths': 13,
        'recovered': 345,
        'active': 2274,
        'critical': 7,
        'tests': 11068,
        'casesPerOneMillion': 69,
        'deathsPerOneMillion': 2,
        'bearing': '0.50',
        'zoom': '3.00',
        'priority': 16,
        'flag': 'https://corona.lmao.ninja/assets/img/flags/af.png',
        'continent': 'Asia'
    }
}


# Create your views here.
def countries_view(request):
    # list of countries show in page
    queryset = Country.objects.all().order_by('priority')
    context = {
        'object_list': queryset,
    }
    return render(request, 'home.html', context)


def database_update(request, *args, **kwargs):
    data_gathered, total, weather, exchange = main()
    Country.objects.all().delete()
    serialized_data = serializers.CountrySerializer(
        data=data_gathered, many=True
    )
    if serialized_data.is_valid():
        serialized_data.save()
    return JsonResponse(data_gathered, JSONEncoder)


class CovidStatisticsAPIView(APIView):
    def get(self, request, format=None):
        try:
            all_contries = Country.objects.all().order_by('priority').values()
            return Response({'data': all_contries}, status=status.HTTP_200_OK)
        except:
            return Response(
                {'status': 'Ohhhh, we had a f**king error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CovidCountryAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        try:
            '''get request from user and return country information with API'''
            country_name = request.GET['country_name']
            country_filter = \
                Country.objects.filter(country__contains=country_name)
            serialized_data = serializers.CountrySerializer(
                country_filter,
                many=True
            )
            data = serialized_data.data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {'status': 'Ohhhh, we had a f**king errot'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def handler404(request, *args, **kwargs):
    return redirect('/')
