# -*- coding: utf-8 -*-
from datetime import datetime
from .colors import Colors as C
from .store_global_data import store_global
from .get_data_api import detachment, total
from .data_injection_json import data_injection
from .firestore_update import store_data_in_firebase
from .kurdistan_weather import firestore_weather_data


def main():
    # Dictionary for all of data gathering
    countries_data = dict()

    # Main Function for gathering data
    # countries_data = data_scraper(countries_data)

    countries_data = data_injection(detachment())

    # Show data will save in firestore

    if countries_data:
        if store_data_in_firebase(countries_data):
            print(u'\n>>> Firebase connection and operation successfully ended.\n# Last Updated at >>> {}.\n'.format(datetime.now()))
        else:
            print(u'\n>>> Every thing is updated.\n# Last Checked at >>> {}.\n'.format(datetime.now()))

    # Get data from api and save in firebase database
    # firestore_weather_data()

    return countries_data


if __name__ == "__main__":
    main()
