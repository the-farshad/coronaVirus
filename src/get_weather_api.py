# -*- coding: utf-8 -*-
import os
import json
import requests
from .file_check import file_abs_path as path
from .file_check import file_exists_check as exist


URL = "https://api.openweathermap.org/data/2.5/weather?q="


def api_key_check():
    filename = 'WeatherAPI.json'
    if exist(filename):
        with open((path() + filename), 'r') as fr:
            api_read = json.load(fr)
        api="&appid="+api_read['api']
        return api
    return False


def get_city_name():
    city_name = dict()
    city_filename = 'kurdistan_city_weather.json'
    if exist(city_filename):
        with open(path() + city_filename, 'r') as fr:
            city_name = json.load(fr)
        return city_name
    return False


def get_weather():
    weather = dict()
    api = api_key_check()
    cities = get_city_name()
    if api:
        if cities:
            for city in cities:
                response = requests.get(URL+city+api, timeout=5)
                response_status = response.status_code
                if response_status == 200:
                    weather[city] = {
                        'kurdish_name': cities[city][0],
                        'priority': cities[city][1],
                        'data': response.json()
                    }
                else:
                    print(city + ' --->> Sorry this city data is not avilable')
        else:
            print('Please add city name')
            return False
    else:
        print('please add you API')
        return False
    return weather


if __name__ == '__main__':
    get_weather()
