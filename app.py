import firebase_admin
from firebase_admin import credentials, firestore
from selenium import webdriver
import time
from collections import defaultdict


class Country(object):
    def __init__(self, country, confirmed=0, deaths=0, recoverd=0):
        self.country = country
        self.confirmed = confirmed
        self.deaths = deaths
        self.recoverd = recoverd

    def to_dict(self):
        contry_dict: {
                u'cityName': self.country,
                u'cases': self.confirmed,
                u'death': self.deaths,
                u'treated': self.recoverd,
                }
        return country_dict


cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
collection = \
        db.collection(u'havalnirtest').document(u'cities').collection(u'cities')

ref = collection.stream()

# for data in ref:
#     print(u'{} => {}'.format(data.id, data.to_dict()))
#     country_database = data.to_dict()
#     if country_database['cityName'] == 'All':
#         collection.document(data.id).update({
#             u'cityName': '',
#         })

# collection.add({
#     'cityName': 'NewDATA',
#     })

URL = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

# Open Website on Browser
driver = webdriver.Chrome()
driver.get(URL)

# Wait until the website finishes loading
time.sleep(5)

# Search within the Confirmed Cases section
confirmed_cases_results = driver.find_elements_by_xpath("//*[@id='ember32']")
total_deaths_results = driver.find_elements_by_xpath("//*[@id='ember74']")
total_recovered_results = driver.find_elements_by_xpath("//*[@id='ember88']")

countries_confirmed = defaultdict(int)
countries_data = dict()
for confirmed_case in confirmed_cases_results:
    # Extract the text containing number of confirmed cases and country
    countries = confirmed_case.find_elements_by_class_name("external-html")
    for country in countries:
        country_confirmed_list = country.text.split(" ", 1)
        countries_data.update({
            country_confirmed_list[1]: {
                u'cityName': country_confirmed_list[1],
                u'cases': int(country_confirmed_list[0].replace(",", "")),
                }})
        countries_confirmed[country_confirmed_list[1]] = \
            int(country_confirmed_list[0].replace(",", ""))
        print(countries_data)


us_death = 0
china_death = 0

for total_death in total_deaths_results:
    # Extract the text containing number of total death and country
    death_countries = total_death.find_elements_by_class_name("external-html")

    for death_country in death_countries:
        death_country_list = \
                death_country.text.replace(" deaths \n", " ").split(" ", 1)

        number_of_death = int(death_country_list[0].replace(",", ""))
        country_name = death_country_list[1].strip()

        if country_name.find("US") >= 0:
            us_death += number_of_death

        if country_name.find("China") >= 0:
            china_death += number_of_death
        else:
            try:
                countries_data[country_name].update({
                   u'death': number_of_death
                    })
            except:
                a = 1

    countries_data['US'].update({
        u'death': us_death,
        })

    countries_data['Mainland China'].update({
        u'death': china_death,
        })


us_recovered = 0
china_recoverd = 0

for total_recovered in total_recovered_results:
    recovered_countries = \
            total_recovered.find_elements_by_class_name("external-html")
    for recovered_country in recovered_countries:
        recovered_countries_list = \
                recovered_country.text.replace("recovered", "").split(" ", 1)

        number_of_recovered = int(recovered_countries_list[0].replace(",", ""))
        country_name = recovered_countries_list[1].strip()

        if country_name.find("US") >= 0:
            us_recovered += number_of_recovered

        if country_name.find("China") >= 0:
            china_recoverd += number_of_recovered
        else:
            try:
                countries_data[country_name].update({
                   u'treated': number_of_recovered
                    })
            except:
                a = 1

    countries_data['US'].update({
        u'treated': us_recovered,
        })

    countries_data['Mainland China'].update({
        u'treated': china_recoverd,
        })

    print(u'\nlast Dict{}'.format(countries_data))
# Quit browser
driver.quit()


for country_data in countries_data:
    collection.add({
        u'cityName': countries_data[country_data]['cityName'],
        u'cases': countries_data[country_data]['cases'],
        u'death': countries_data[country_data]['death'] if 'death' in countries_data[country_data] else 0,
        u'treated': countries_data[country_data]['treated'] if 'treated' in countries_data[country_data] else 0
        })
