import requests
from colors import Colors as C
import time
URL_ALL = 'https://corona.lmao.ninja/all'
URL_COUNTRIES = 'https://corona.lmao.ninja/countries'


def total():
    response_all = requests.get(URL_ALL)
    satus_code_all = response_all.status_code
    if satus_code_all == 200:
        data_all = response_all.json()
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
