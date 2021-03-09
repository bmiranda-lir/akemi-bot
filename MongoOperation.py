import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

db = MongoClient(os.getenv("CONN_STRING"))


def is_database_alive():
    try:
        db.admin.command('ismaster')
        return "Database: Healthy"
    except ConnectionFailure:
        return "Database: Currently unavailable"
