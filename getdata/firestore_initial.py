import firebase_admin
from firebase_admin import credentials, firestore
from .file_check import file_abs_path as path


def firebase_initial():
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate(path() + 'ServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


if __name__ == '__main__':
    firebase_initial()
