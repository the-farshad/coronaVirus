from .models import Country
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    country = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        max_length=50
    )
    countryKurdishName = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        max_length=50
    )
    _id = serializers.IntegerField(
        required=True,
        min_value=0,
        max_value=32767
    )
    iso2 = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        max_length=2
    )
    iso3 = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        max_length=3
    )
    latitude = serializers.DecimalField(
        required=False,
        allow_null=True,
        max_digits=14,
        decimal_places=10
    )
    lat = serializers.DecimalField(
        required=False,
        allow_null=True,
        max_digits=10,
        decimal_places=6
    )
    longitude = serializers.DecimalField(
        allow_null=True,
        required=False,
        max_digits=14,
        decimal_places=10
    )
    long = serializers.DecimalField(
        allow_null=True,
        required=False,
        max_digits=10,
        decimal_places=6
    )
    cases = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647

    )
    todayCases = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    deaths = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    todayDeaths = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    recovered = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    active = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    critical = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    tests = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    casesPerOneMillion = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    deathsPerOneMillion = serializers.IntegerField(
        required=True,
        allow_null=False,
        min_value=0,
        max_value=2147483647
    )
    bearing = serializers.DecimalField(
        required=False,
        allow_null=True,
        max_digits=4,
        decimal_places=2
    )
    zoom = serializers.DecimalField(
        required=False,
        allow_null=True,
        max_digits=4,
        decimal_places=2
    )
    priority = serializers.IntegerField(
        required=True,
        allow_null=False,
    )
    flag = serializers.URLField(
        max_length=200
    )
    continent = serializers.CharField(
        max_length=20
    )

    class Meta:
        model = Country
        fields = '__all__'
