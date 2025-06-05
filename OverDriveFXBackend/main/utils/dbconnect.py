from pymongo import MongoClient
from django.conf import settings
def connect_db(colecction_name):
    client = MongoClient(settings.MONGODB_CONFIG['HOST'], settings.MONGODB_CONFIG['PORT'])
    db = client[settings.MONGODB_CONFIG['DB_NAME']]
    collection = db[colecction_name]
    return collection