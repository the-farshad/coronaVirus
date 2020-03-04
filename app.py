import firebase_admin
from firebase_admin import credentials, firestore
from selenium import webdriver
import time
from collections import defaultdict


cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection(u'cities')
collection.add({
    u'cityName': 'TestData',
    })

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
for confirmed_case in confirmed_cases_results:
    # Extract the text containing number of confirmed cases and country
    countries = confirmed_case.find_elements_by_class_name("external-html")
    for country in countries:
        country_attr = country.text.split(" ", 1)
        print(country_attr)
        countries_confirmed[country_attr[1]] = int(country_attr[0].replace(",", ""))
        print(countries_confirmed[country_attr[1]])
        print(country.text)

countries_deaths = defaultdict(int)
for total_death in total_deaths_results:
    # Extract the text containing number of total death and country
    death_countries = total_death.find_elements_by_class_name("external-html")
    for death_country in death_countries:
        death_country_list = death_country.text.replace(" deaths \n", " ").split(" ", 1)
        print(death_country_list)
        countries_deaths[death_country_list[1].strip()] = int(death_country_list[0].replace(",", ""))
        print(countries_deaths)

countries_recovered = defaultdict(int)
for total_recovered in total_recovered_results:
    recovered_countries = total_recovered.find_elements_by_class_name("external-html")
    for recovered_country in recovered_countries:
        recovered_countries_list = recovered_country.text.replace("recovered", "").split(" ", 1)
        print(recovered_countries_list)
        countries_recovered[recovered_countries_list[1].strip()] = int(recovered_countries_list[0].replace(",", ""))
        print(countries_recovered)

# Quit browser
driver.quit()
