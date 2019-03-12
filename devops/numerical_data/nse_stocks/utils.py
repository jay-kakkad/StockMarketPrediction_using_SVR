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
    def update_inter_day_data(self,stock,source,start_date,end_date,collection_name):
        client = Database().initialize_db()
        db = client["jsrdb"]
        df = web.DataReader(stock,source,start_date,end_date)
        df.insert(0, "Date", df.index)
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        records = json.loads(df.T.to_json(date_format="iso")).values()
        try:
            db[collection_name].insert_many(records)
            print("Inserted " + str(len(records)) + " Values")
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


    def delete_data(self,client,collectiona_name,query):
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


class Technical_Indicators:
    OBJ = None

    def __init__(self,obj):
        self.OBJ = obj

    def indicator_MA(self,window_size):
        df = self.OBJ.retrieve_inter_day_data()
        ma = df["Close"].rolling(window=window_size).mean()
        return ma

    def indicator_EMA(self,windows_size):
        df = self.OBJ.retrieve_inter_day_data()
        ema = df["Close"].ewm(span=windows_size, adjust=False)
        return ema

    def indicator_VWAP(self):
        df = self.OBJ.retrieve_inter_day_data()
        q = df["Close"]
        p = df["Volume"]
        vmap = (p * q).cumsum() / q.cumsum()
        return vmap

    def indicator_MACD(self):
        return None

    def indicator_STOCH(self):
        return None

    def indicator_RSI(self):
        return None

    def indicator_ADX(self):
        return None

    def indicator_BBANDS(self):
        return None

    def indicator_AD(self):
        return None

    def indicator_OBV(self):
        return None



if __name__ == "__main__":
    Database().main()
