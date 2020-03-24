# -*- coding: utf-8 -*-
import time
import json
from datetime import datetime
import os
from colors import Colors as C
from get_data_api import detachment, total
from data_injection_json import data_injection
from firestore_update import store_data_in_firebase
from store_global_data import store_global


def main():
    # Dictionary for all of data gathering
    countries_data = dict()

    # Main Function for gathering data
    # countries_data = data_scraper(countries_data)

    countries_data = data_injection(detachment())
    print(C.WARNING, store_global(total()), C.ENDC)

    # Show data will save in firestore
    print(u">>> ALL DATA GATHERED >>>\n{}\n\n".format(countries_data))

    if countries_data:
        if store_data_in_firebase(countries_data):
            print(u'\n>>> Firebase connection and operation successfully ended.\n# Last Updated at >>> {}.\n'.format(datetime.now()))
    else:
        print(u'\n>>> Every thing is updated.\n# Last Checked at >>> {}.\n'.format(datetime.now()))

if __name__ == "__main__":
    main()
