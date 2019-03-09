from datetime import date

import pandas as pd
import pymongo
import pandas_datareader.data as web
import datetime as dt
import numpy
import json
import pyrebase


# To fetch historical data
# Stock = Name of Stock
# Source = Name of source from where data will be fetched
# start_date,end_date = start and end dates between which all data will be fetched

def update_historical_data(stock,source,start_date,end_date,collection_name):
    client = intialize_db()
    db = client["jsrdb"]
    df = web.DataReader(stock,source,start_date,end_date)
    df.insert(0, "Date", df.index)
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    # print(df["Date"].head())
    records = json.loads(df.T.to_json(date_format="iso")).values()
    # print(records)
    try:
        db[collection_name].insert_many(records)
        print("Inserted " + str(len(records)) + " Values")
        client.close()
    except Exception as e:
        print(str(e))


def update_data(collection_name,data):
    client = intialize_db()
    db = client["jsrdb"]
    result = db[collection_name].find()
    client[collection_name].insert_many(data).inserted_ids


def retireve_data(collection_name,query):
    client = intialize_db()
    db = client["jsrdb"]
    result = list(db[collection_name].find(query))
    result = pd.DataFrame(result)
    # print(result)
    client.close()
    return result

def delete_data(client,collectiona_name,query):
    client = intialize_db()
    db = client["jsrdb"]
    db[collectiona_name].delete_many(query)
    search = db[collectiona_name].find(query)
    if search == None:
        return True
    else:
        return False


def intialize_db(): return pymongo.MongoClient("mongodb+srv://jsr:g9TdO0CTga2Ncsvu@cluster0-10kli.gcp.mongodb.net/test?retryWrites=true")


def main():
    print("Tested")


if __name__ == "__main__":
    main()
