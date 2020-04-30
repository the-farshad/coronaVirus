import os
import json
from get_data_api import detachment


def geo():
    export = dict()
    filename = 'information.json'

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            datastore = json.load(f)

        for data in datastore:
            export.update({
                    datastore[data]['cityName']: {
                        u'countryKurdishName': datastore[data]['countryName_KU'],
                        u'bearing': 0.5,
                        u'latitude': datastore[data]['latLong'][0],
                        u'longitude': datastore[data]['latLong'][1],
                        u'zoom': datastore[data]['zoom'],
                        u'priority': datastore[data]['priority'],
                        }
                    })
    export2 = dict()
    import_dict = detachment()
    import_dict2 = import_dict
    for country in import_dict:
        for data in export:
            data_lower = data
            country_lower = country['country']
            if data_lower.find(country_lower) != -1:
                export2.update({
                    country['country']: {
                            u'countryKurdishName': export[data]['countryKurdishName'],
                            u'cases': 0,
                            u'todayCases': 0,
                            u'deaths': 0,
                            u'todayDeaths': 0,
                            u'recovered': 0,
                            u'critical': 0,
                            u'bearing': 0.5,
                            u'latitude': export[data]['latitude'],
                            u'longitude': export[data]['longitude'],
                            u'zoom': export[data]['zoom'],
                            u'priority': export[data]['priority'],
                            }
                        })
                print('Saver DATA  >> {} ====>> Get DATA {}'.format(
                    data,
                    country['country']
                    ))
                print(country)
                import_dict2.remove(country)

    for new_data in import_dict2:
        export2.update({
            new_data['country']: {
                    u'countryKurdishName': '',
                    u'cases': 0,
                    u'todayCases': 0,
                    u'deaths': 0,
                    u'todayDeaths': 0,
                    u'recovered': 0,
                    u'critical': 0,
                    u'bearing': 0.5,
                    u'latitude': 0,
                    u'longitude': 0,
                    u'zoom': 3,
                    u'priority': 999,
                    }
                })

    with open('geodata.json', 'w') as f:
        json.dump(export, f)
    with open('raw_information.json', 'w') as f:
        json.dump(export, f)


if __name__ == '__main__':
    geo()
