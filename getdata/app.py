# -*- coding: utf-8 -*-
from datetime import datetime
from .store_global_data import store_global
from .get_data_api import detachment, total
from .data_injection_json import data_injection
from .firestore_update import store_data_in_firebase
from .kurdistan_weather import firestore_weather_data
from .exchange_rate_firestore import firestore_rate_data


def main():
    # Dictionary for all of data gathering
    countries_data = dict()

    # Main Function for gathering data
    # countries_data = data_scraper(countries_data)

    countries_data = data_injection(detachment())

    # Store total statistics in database
    world_statistics = store_global(total())

    # Show data will save in firestore
    if countries_data:
        if store_data_in_firebase(countries_data):
            print(
                u'\n>>> Firebase connection and operation successfully \
                ended.\n# Last Updated at >>> {}.\n'.format(
                    datetime.now()
                )
            )
        else:
            print(
                u'\n>>> Every thing is updated.\n#Last Checked \
                at >>> {}.\n'.format(
                    datetime.now()
                )
            )

    # Get Kurdistan weather data from api and save in to firebase database
    weather = firestore_weather_data()

    # Get Exchange IQD rae data from api and save in to firebase database
    exchange = firestore_rate_data()

    country_list = list()
    for country in countries_data:
        if countries_data[country]['_id'] is not None:
            countries_data[country]['updated'] = \
                datetime.fromtimestamp(
                    countries_data[country]['updated'] / 1000
                )
            country_list.append(countries_data[country])

    return country_list, world_statistics, weather, exchange


if __name__ == "__main__":
    main()
