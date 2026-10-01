import sys
import os

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

import pymongo
import certifi
from dotenv import load_dotenv

ca = certifi.where()

load_dotenv()


class MongoDBClient:
    client = None
    
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                database_url = os.getenv(MONGODB_URL_KEY)
                if database_url is None:
                    raise Exception(f"Environment variable: {MONGODB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(database_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database_name = database_name
            self.database = self.client[database_name]
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)
            