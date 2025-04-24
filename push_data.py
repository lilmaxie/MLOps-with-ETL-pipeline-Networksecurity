import os 
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
print(MONGO_DB_URI)


import certifi # for SSL certificate verification
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        """
        output from: 
        A    B    C
        1.0  2.0  3.0
        4.0  5.0  6.0
        to: [
            {A: 1.0, B: 2.0, C: 3.0}, 
            {A: 4.0, B: 5.0, C: 6.0}
            ]
        """
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            # convert to json format by transposing the data frame and then converting to a list of dictionaries
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys) 
        
    def insert_data_mongodb(self, records, database, collection):
        """
        Insert data into MongoDB collection
        """
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "LILMAXIE"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records=records, database=DATABASE, collection=Collection)
    print(no_of_records)