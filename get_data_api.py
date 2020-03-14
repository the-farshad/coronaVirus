import requests
from colors import Colors as C
import time
URL_ALL = 'https://corona.lmao.ninja/all'
URL_COUNTRIES = 'https://corona.lmao.ninja/countries'


def total():
    world = dict()
    response_all = requests.get(URL_ALL)
    satus_code_all = response_all.status_code
    if satus_code_all == 200:
        data_all = response_all.json()
        world = {
            'world': {
                u'countryKurdishName': 'جیهان',
                u'cases': data_all['cases'],
                u'recovered': data_all['recovered'],
                u'deaths': data_all['deaths'],
                u'todayCases': 0,
                u'todayDeaths': 0,
                u'critical': 0,
                u'latitude': 36.1674,
                u'longitude': 43.9812,
                u'bearing': 1,
                u'zoom': 4,
                u'priority': -1,
                }
            }
        return data_all
    else:
        return False


def detachment():
    response_countries = requests.get(URL_COUNTRIES)
    satus_code_countries = response_countries.status_code
    if satus_code_countries == 200:
        data_countries = response_countries.json()
        return data_countries
    else:
        return False


def get_data_from_api():
    for data in detachment():
        time.sleep(.5)
        print(C.OKBLUE, data, C.ENDC)
    print(C.WARNING, total(), C.ENDC)


if __name__ == '__main__':
    get_data_from_api()
