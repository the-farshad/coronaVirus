# -*- coding: utf-8 -*-
import os
import json
import requests
from .file_check import file_abs_path as path
from .file_check import file_exists_check as exist


URL = "http://data.fixer.io/api/latest?access_key="
SYMBOLS = "&symbols=IQD,EUR,USD,GBP,CAD,JYP,IRR,TRY"


def api_key_check():
    filename = 'exchange_rate_api.json'
    if exist(filename):
        with open((path() + filename), 'r') as fr:
            api_read = json.load(fr)
        return api_read['api']+SYMBOLS
    return False


def get_rate():
    rate = dict()
    api = api_key_check()
    if api:
        response = requests.get(URL+api, timeout=5)
        response_status = response.status_code
        if response_status == 200:
            rate = response.json()
            print(rate)
        else:
            print("Sorry, We had some error >> " + response_status)
            return False
    else:
        print('please add you API')
        return False
    return rate


if __name__ == '__main__':
    get_rate()
