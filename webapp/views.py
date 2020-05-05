# -*- codeing: utf-8 -*-

from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Country
from getdata import main
from . import serializers


# Create your views here.
def countries_view(request):
    # list of countries show in page
    queryset = Country.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, 'home.html', context)


class DatabaseUpdate(APIView):
    def post(self, request, format=None, *args, **kwargs):
        try:
            data_gathered, total, weather, exchange = main()
            queryset = Country.objects.all()
            serialized_data = serializers.CountrySerializer(
                data=data_gathered,
                many=True
            )
            if serialized_data.is_valid():
                datasets = serialized_data.data
                for data in datasets:
                    country_key = data['_id']
                    flag = queryset.filter(
                        _id=country_key
                    ).update(**data)
                    if flag == 0:
                        queryset.create(**data)
            else:
                print(serialized_data.errors)
            return Response(
                {
                    'data': serialized_data.data
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {'status': 'Ohhhh, we had a f**king error' + e},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CovidStatisticsAPIView(APIView):
    def get(self, request, format=None):
        try:
            all_contries = Country.objects.all().values()
            return Response({'data': all_contries}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'status': 'Ohhhh, we had a f**king error' + e},
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
            return Response(
                {
                    'data': data
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'status': 'Ohhhh, we had a f**king error' + e},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def handler404(request, *args, **kwargs):
    return redirect('/')
