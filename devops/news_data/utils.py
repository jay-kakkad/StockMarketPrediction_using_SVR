from datetime import date

import pandas as pd
import pymongo
import pandas_datareader.data as web
import datetime as dt
import numpy
import json


# To fetch inter_day data
# Stock = Name of Stock
# Source = Name of source from where data will be fetched
# start_date,end_date = start and end dates between which all data will be fetched

class Database:
    def insert_data(self,collection_name,feeds):
        client = Database().initialize_db()
        db = client["jsrdb"]
        try:
            db[collection_name].insert_many(feeds)
            print("Inserted " + str(len(feeds)) + " Values")
            client.close()
        except Exception as e:
            print(str(e))


    def retireve_data(self,collection_name,query):
        client = Database().initialize_db()
        db = client["jsrdb"]
        result = list(db[collection_name].find(query))
        result = pd.DataFrame(result)
        # print(result)
        client.close()
        return result


    def delete_data(self,collectiona_name,query):
        client = Database().initialize_db()
        db = client["jsrdb"]
        db[collectiona_name].delete_many(query)
        search = db[collectiona_name].find(query)
        if search == None:
            return True
        else:
            return False


    def initialize_db(self):
        return pymongo.MongoClient("mongodb+srv://jsr:tMDSfCpnqyjSy3Pw@cluster0-10kli.gcp.mongodb.net/test?retryWrites=true")


    def main(self):
        print("Tested")





if __name__ == "__main__":
    Database().main()
