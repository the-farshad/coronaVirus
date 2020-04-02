import firebase_admin
from firebase_admin import credentials, firestore
from colors import Colors as C
from get_data_api import total
from file_check import file_abs_path as path

def firebase_init():
    cred = credentials.Certificate(path() + 'ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    collection = \
        db.collection(u'havalnir').document(u'cities').collection(u'total').document(u'world')

    return collection


def store_global(global_data):
    print(C.BOLD, C.OKBLUE, global_data, C.ENDC)
    collection = firebase_init()
    collection.set({
        u'cases': global_data['cases'],
        u'recovered': global_data['recovered'],
        u'deaths': global_data['deaths'],
        })
    print(C.OKGREEN, global_data, C.ENDC)


if __name__ == '__main__':
    store_global(total())
