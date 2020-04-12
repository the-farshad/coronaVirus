import firebase_admin
from firebase_admin import credentials, firestore
from .data_injection_json import data_injection
from .colors import Colors as C
from .file_check import file_abs_path as path
from .firestore_initial import firebase_initial as fire


def firestore_init():
    db = fire()
    collection = \
        db.collection(u'havalnir').document(u'cities').collection(u'cities')

    return collection


# Read data from dictionary and store  in Firebase
def store_data_in_firebase(input_data):
    countries_data = input_data.copy()
    collection = firestore_init()
    ref = collection.stream()
    for firebase_data in ref:
        info = firebase_data.to_dict()
        id_ = firebase_data.id
        if info != {}:
            courser = info['cityName']
            if courser in countries_data:
                if info['cases'] != countries_data[courser]['cases'] or info['death'] != countries_data[courser]['deaths'] or info['treated'] != countries_data[courser]['recovered']:
                    latitude = countries_data[courser]['latitude']
                    longitude = countries_data[courser]['longitude']
                    try:
                        collection.document(id_).update({
                            u'cityName': courser,
                            u'countryName_KU': countries_data[courser]['countryKurdishName'],
                            u'cases': countries_data[courser]['cases'],
                            u'death': countries_data[courser]['deaths'],
                            u'treated': countries_data[courser]['recovered'],
                            u'todayCases': countries_data[courser]['todayCases'],
                            u'todayDeaths': countries_data[courser]['todayDeaths'],
                            u'critical': countries_data[courser]['critical'],
                            u'bearing': countries_data[courser]['bearing'],
                            u'latLong': firestore.GeoPoint(latitude, longitude),
                            u'priority': countries_data[courser]['priority'],
                            u'zoom': countries_data[courser]['zoom'],
                            })
                    except:
                        print(u'We have some problem!')
                    else:
                        print(u"{}DATA UPDATED ----->>> {}{} >> {}. ######".format(
                            C.WARNING,
                            C.ENDC,
                            courser,
                            info
                            ))
                del countries_data[courser]
    for new_country in countries_data:
        print(u"{}NEW COUNTRY ADDED ---->>>{} {} >> {}. *****".format(
            C.FAIL,
            C.ENDC,
            new_country,
            countries_data[new_country]
            ))

        latitude = countries_data[new_country]['latitude']
        longitude = countries_data[new_country]['longitude']
        collection.add({
            u'cityName': new_country,
            u'cases': countries_data[new_country]['cases'],
            u'death': countries_data[new_country]['deaths'],
            u'treated': countries_data[new_country]['recovered'],
            u'countryName_KU': countries_data[new_country]['countryKurdishName'],
            u'critical': countries_data[new_country]['critical'],
            u'todayCases': countries_data[new_country]['todayCases'],
            u'todayDeaths': countries_data[new_country]['todayDeaths'],
            u'bearing': countries_data[new_country]['bearing'],
            u'latLong': firestore.GeoPoint(latitude, longitude),
            u'priority': countries_data[new_country]['priority'],
            u'zoom': countries_data[new_country]['zoom'],
            })
    return True

if __name__ == '__main__':
    store_data_in_firbase(data_injection())
