from selenium import webdriver
import time
import json
from datetime import datetime
import os
from colors import Colors as C
from get_data_api import detachment, total
from data_injection_json import data_injection
from firestore_update import store_data_in_firebase
from store_global_data import store_global


# Scrape list of countries they have confirmed cases
def scrape_confirmed_cases(confirmed_cases_results, countries_data):
    for confirmed_case in confirmed_cases_results:
        # Extract the text containing number of confirmed cases and country
        countries = confirmed_case.find_elements_by_class_name("external-html")

        # Extract name of countries and number of confirmed cases and store in dictionary
        for country in countries:
            country_confirmed_list = country.text.split(" ", 1)
            countries_data.update({
                country_confirmed_list[1]: {
                    u'cityName': country_confirmed_list[1],
                    u'countryName_KU': '',
                    u'bearing': 0.5,
                    u'latLong': [0,0],
                    u'zoom': 3,
                    u'cases': int(country_confirmed_list[0].replace(",", "")),
                    u'treated': 0,
                    u'priority': 999,
                    }})

    # Find all of cases are confirmed and return them
    return countries_data


# Scrape total of country has death case
def scrape_death_cases(total_deaths_results, countries_data):

    us_death = 0
    china_death = 0

    for total_death in total_deaths_results:
        # Extract the text containing number of total death and country
        death_countries = \
            total_death.find_elements_by_class_name("external-html")

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

        countries_data['China'].update({
            u'death': china_death,
            })

    return countries_data


def scrape_recovered_cases(total_recovered_results, countries_data):
    us_recovered = 0
    china_recovered = 0

    for total_recovered in total_recovered_results:
        recovered_countries = \
                total_recovered.find_elements_by_class_name("external-html")
        for recovered_country in recovered_countries:
            recovered_countries_list = \
                recovered_country.text.replace("recovered", "").split(" ", 1)

            number_of_recovered = \
                int(recovered_countries_list[0].replace(",", ""))
            country_name = recovered_countries_list[1].strip()

            if country_name.find("US") >= 0:
                us_recovered += number_of_recovered

            if country_name.find("China") >= 0:
                china_recovered += number_of_recovered
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

        countries_data['China'].update({
            u'treated': china_recovered,
            })

    return countries_data


def data_scraper(data_gathered):
    URL = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

    # Open Website on Browser
    driver = webdriver.Chrome()
    driver.get(URL)

    # Wait until the website finishes loading
    time.sleep(6)

    # Scrape all of of countries have confirmed case
    confirmed_cases_results = \
        driver.find_elements_by_xpath("//*[@id='ember33']")

    data_gathered = scrape_confirmed_cases(confirmed_cases_results, data_gathered)

    # Scrape all of of countries have confirmed death
    total_deaths_results = driver.find_elements_by_xpath("//*[@id='ember83']")

    data_gathered = scrape_death_cases(total_deaths_results, data_gathered)

    # Scrape all of of countries have confirmed recovered
    total_recovered_results = \
        driver.find_elements_by_xpath("//*[@id='ember97']")

    data_gathered = \
        scrape_recovered_cases(total_recovered_results, data_gathered)

    # Quit browser
    driver.quit()

    return data_gathered

def check_data(info):
    print(info)
    filename = 'information.json'

    if os.path.exists(filename):
        #Read JSON data into the datastore variable
        with open(filename, 'r') as f:
            datastore = json.load(f)


        for field in datastore:
            try:
                info[field]['latLong'] = datastore[field]['latLong']
                info[field]['countryName_KU'] = datastore[field]['countryName_KU']
                info[field]['priority'] = datastore[field]['priority']
            except:
                print(u'{}{}{} ---> We can\'t find in this country in our CSV'.format(Colors.FAIL, field ,Colors.ENDC))
            else:
                print(u'{}{}{} ---> This Field is updated'.format(Colors.OKGREEN, field ,Colors.ENDC))
        if datastore == info:
            return False

        # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(info, f)
    return info


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
