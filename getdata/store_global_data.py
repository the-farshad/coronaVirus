import firebase_admin
from firebase_admin import credentials, firestore
from .colors import Colors as C
from .get_data_api import total
from .firestore_initial import firebase_initial as fire


def firestore_init():
    db = fire()
    collection = \
        db.collection(u'havalnir').document(u'cities').collection(u'total').document(u'world')

    return collection


def store_global(global_data):
    collection = firestore_init()
    collection.set({
        u'cases': global_data['cases'],
        u'kurdishName': global_data['kurdishName'],
        u'recovered': global_data['recovered'],
        u'deaths': global_data['deaths'],
        u'todayCases': global_data['todayCases'],
        u'todayDeaths': global_data['todayDeaths'],
        u'critical': global_data['critical']
        })
    print(C.OKGREEN, global_data, C.ENDC)
    return global_data


if __name__ == '__main__':
    store_global(total())
