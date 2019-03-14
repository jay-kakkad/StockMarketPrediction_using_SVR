
import pandas as pd
import pymongo
import pandas_datareader.data as web
import json


# To fetch inter_day data
# Stock = Name of Stock
# Source = Name of source from where data will be fetched
# start_date,end_date = start and end dates between which all data will be fetched

class Database:
    def inter_day_data(self,stock,source,start_date,end_date,collection_name):
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

    def store_data(self,df,collection_name):
        client = Database().initialize_db()
        db = client["jsrdb"]
        try:
            records = json.loads(df.T.to_json(date_format="iso")).values()
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
    DF = None

    def __init__(self,obj=None):
        self.OBJ = obj
        self.DF =obj.retrieve_inter_day_data()

    def daily_update(self):

        return None

    def MA(self,window_size,adj_close):
        MA = adj_close.rolling(window=window_size).mean()
        return MA

    def EMWA(self,windows_size,adj_close):
        EMWA =adj_close.ewm(span=windows_size,adjust=False).mean()
        return EMWA

    def VMAP(self,adj_close,volume):
        q = adj_close
        p = volume
        VMAP = (p * q).cumsum() / q.cumsum()
        return VMAP

    def MACD(self,data,obj):
        MACD = Technical_Indicators(obj).EMWA(26,data)-Technical_Indicators(obj).EMWA(12,data)
        return MACD

    def STOK(self,close,low,high,n):
        STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
        return STOK

    def STOD(self,STOK):
        STOD = STOK.rolling(3).mean()
        return STOD

    def RSI(self,delta,n):
        dUp, dDown = delta.copy(), delta.copy()
        dUp[dUp < 0] = 0
        dDown[dDown > 0] = 0
        RolUp = dUp.rolling(n).mean()
        RolDown = dDown.rolling(n).mean()
        RS = RolUp/RolDown
        return RS

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
