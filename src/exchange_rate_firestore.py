from datetime import datetime

from .firestore_initial import firebase_initial as fire
from .get_exchange_rate_api import get_rate


def firestore_init():
    db = fire()
    collection = \
            db.collection(u'havalnir').document(u'exchange').collection(u'iqd_rate')

    return collection


def firestore_rate_data():
    collection = firestore_init()
    rate_data = get_rate()
    if rate_data:
        update_time = rate_data['timestamp']
        rates = rate_data['rates']

        for rate in rates:
            details = rates[rate]
            collection.document(rate).set({
                'currency': rate,
                'rate': 100 * (rates['IQD']/rates[rate]),
                })
        collection.document('updated').set({'updated': datetime.fromtimestamp(update_time)})
    else:
        print('Ohhh, we had a problem! :| ')



if __name__ == '__main__':
    firestore_rate_data()
