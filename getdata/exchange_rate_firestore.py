from datetime import datetime

from .firestore_initial import firebase_initial as fire
from .get_exchange_rate_api import get_rate


PRIORITY = {"USD":1, "GBP":2, "EUR":3, "TRY":4, "IRR":5, "IQD":6}

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
            collection.document(rate).set({
                'currency': rate,
                'priority': PRIORITY[rate],
                'rate': 100 * (rates['IQD']/rates[rate]),
                })
        collection.document('updated').set({'updated': datetime.fromtimestamp(update_time)})
    else:
        print('Ohhh, we had a problem! :| ')
    return rates



if __name__ == '__main__':
    firestore_rate_data()
