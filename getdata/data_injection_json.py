import json

from .get_data_api import detachment
from .kurdistan_corona_cases import kurdistan_data_gathered as kurdistan
from .file_check import file_exists_check as exist
from .file_check import file_abs_path as path


def data_injection(last_api_data):
    processed_data = dict()

    processed_data.update(kurdistan())

    new_country_added = list()
    filename_raw = 'raw_information.json'
    filename_processed = 'processed_information.json'

    if exist(filename_raw):
        with open((path() + filename_raw), 'r') as fr:
            data_raw = json.load(fr)

    for api_data in last_api_data:
        country = api_data['country']
        if country in data_raw:
            processed_data.update({
                country: {
                    u'country': country,
                    u'countryKurdishName': data_raw[country]['countryKurdishName'],
                    u'cases': api_data['cases'],
                    u'todayCases': api_data['todayCases'],
                    u'deaths': api_data['deaths'],
                    u'todayDeaths': api_data['todayDeaths'],
                    u'recovered': api_data['recovered'],
                    u'critical': api_data['critical'],
                    u'bearing': data_raw[country]['bearing'],
                    u'latitude': data_raw[country]['latitude'],
                    u'longitude': data_raw[country]['longitude'],
                    u'zoom': data_raw[country]['zoom'],
                    u'priority': data_raw[country]['priority'],
                    u'active': api_data['active'],
                    u'casesPerOneMillion': api_data['casesPerOneMillion'],
                    u'deathsPerOneMillion': api_data['deathsPerOneMillion'],
                    u'tests': api_data['tests'],
                    u'testsPerOneMillion': api_data['testsPerOneMillion'],
                    u'_id': api_data['countryInfo']['_id'],
                    u'iso2': api_data['countryInfo']['iso2'],
                    u'iso3': api_data['countryInfo']['iso3'],
                    u'lat': api_data['countryInfo']['lat'],
                    u'long': api_data['countryInfo']['long'],
                    u'flag': api_data['countryInfo']['flag'],
                    u'updated': api_data['updated'],
                    u'continent': api_data['continent'],
                    }
                })
        else:
            new_country_added.append(api_data)
            processed_data.update({
                country: {
                    u'country': country,
                    u'countryKurdishName': '',
                    u'cases': api_data['cases'],
                    u'todayCases': api_data['todayCases'],
                    u'deaths': api_data['deaths'],
                    u'todayDeaths': api_data['todayDeaths'],
                    u'recovered': api_data['recovered'],
                    u'critical': api_data['critical'],
                    u'active': api_data['active'],
                    u'casesPerOneMillion': api_data['casesPerOneMillion'],
                    u'deathsPerOneMillion': api_data['deathsPerOneMillion'],
                    u'tests': api_data['tests'],
                    u'testsPerOneMillion': api_data['testsPerOneMillion'],
                    u'_id': api_data['countryInfo']['_id'],
                    u'iso2': api_data['countryInfo']['iso2'],
                    u'iso3': api_data['countryInfo']['iso3'],
                    u'lat': api_data['countryInfo']['lat'],
                    u'long': api_data['countryInfo']['long'],
                    u'flag': api_data['countryInfo']['flag'],
                    u'bearing': 0.5,
                    u'latitude': 0,
                    u'longitude': 0,
                    u'zoom': 3,
                    u'priority': 999,
                    u'updated': api_data['updated'],
                    u'continent': api_data['continent'],
                    }
                })

    if len(new_country_added) != 0:
        for new_country in new_country_added:
            data_raw.update({
                new_country['country']: {
                    u'countryKurdishName': '',
                    u'bearing': 0.5,
                    u'latitude': 0,
                    u'longitude': 0,
                    u'zoom': 3,
                    u'priority': 999,
                    }
                })
        with open(filename_raw, 'w') as fr:
            json.dump(data_raw, fr)

    with open(filename_processed, 'w') as pf:
        json.dump(processed_data, pf)

    return processed_data


if __name__ == '__main__':
    data_injection(detachment())
