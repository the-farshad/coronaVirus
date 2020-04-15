from .firestore_initial import firebase_initial as fire
from .get_weather_api import get_weather
from datetime import datetime


def firestore_init():
    db = fire()
    collection = \
            db.collection(u'havalnir').document(u'cities').collection(u'weather')
    return collection

def firestore_weather_data():
    collection = firestore_init()
    weathers_data = get_weather()
    if weathers_data:
        for city_weather in weathers_data:
            details = weathers_data[city_weather]
            collection.document(city_weather).set({
                    'city_name': city_weather,
                    'kurdish_name':details['kurdish_name'],
                    'longitude': details['data']['coord']['lon'],
                    'latitude': details['data']['coord']['lat'],
                    'temperature': round((details['data']['main']['temp'] - 273.15), 2),
                    'feels_like': round((details['data']['main']['feels_like'] - 273.15), 2),
                    'temperature_min': round((details['data']['main']['temp_min'] - 273.15), 2),
                    'temperature_max': round((details['data']['main']['temp_max'] - 273.15), 2),
                    'pressure': details['data']['main']['pressure'],
                    'humidity': details['data']['main']['humidity'],
                    'wind_speed': (details['data']['wind']['speed']),
                    'sunrise': datetime.fromtimestamp(details['data']['sys']['sunrise']),
                    'sunset': datetime.fromtimestamp(details['data']['sys']['sunset']),
                    'weather_main': details['data']['weather'][0]['main'],
                    'weather_description': details['data']['weather'][0]['description'],
                    'weather_icon': details['data']['weather'][0]['icon'],
                    })
    else:
        print('Ohhh, we had a problem! :| ')



if __name__ == '__main__':
    firestore_weather_data()
