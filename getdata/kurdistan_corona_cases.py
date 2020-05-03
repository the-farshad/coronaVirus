from time import time
import requests
import bs4
from .colors import Colors as C


URL = 'https://gov.krd/coronavirus-en/situation-update/#moh-monitoring'


def kurdistan_data_gathered():
    kurdistan = dict()
    respose = requests.get(URL)
    if respose.status_code == 200:
        content = bs4.BeautifulSoup(respose.content, 'lxml')
        select = content.select('table tbody tr td p')
        for element in select:
            text = element.text
            find_total_confirmed = text.find('Total confirmed cases:')
            find_total_recovered = text.find('Total recovered:')
            find_total_deaths = text.find('Total deaths:')
            find_total_active = text.find('Total active cases: ')
            if find_total_confirmed != -1:
                kurdistan.update({
                    'Kurdistan': {
                        u'country': 'Kurdistan',
                        u'countryKurdishName': 'کوردستان',
                        u'cases': int(text.split(':')[1]),
                        u'todayCases': 0,
                        u'todayDeaths': 0,
                        u'critical': 0,
                        u'latitude': 36.1674,
                        u'longitude': 43.9812,
                        u'bearing': 1,
                        u'zoom': 4,
                        u'priority': -1,
                        u'deathsPerOneMillion': 0,
                        u'casesPerOneMillion': 0,
                        u'tests': 0,
                        u'testsPerOneMillion': 0,
                        u'_id': 0,
                        u'iso2': 'kd',
                        u'iso3': 'krd',
                        u'lat': 36,
                        u'long': 43,
                        u'flag': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Flag_of_Kurdistan.svg',
                        u'updated': (time() * 1000),
                        u'continent': 'Asia'
                        }
                    })

            elif find_total_recovered != -1:
                kurdistan['Kurdistan'].update({
                    u'recovered': int(text.split(':')[1])
                    })

            elif find_total_deaths != -1:
                kurdistan['Kurdistan'].update({
                    u'deaths': int(text.split(':')[1])
                    })

            elif find_total_active != -1:
                kurdistan['Kurdistan'].update({
                    u'active': int(text.split(':')[1])
                    })

        print(C.FAIL, C.UNDERLINE, kurdistan, C.ENDC)
        return kurdistan
    else:
        return False


if __name__ == '__main__':
    kurdistan_data_gathered()
