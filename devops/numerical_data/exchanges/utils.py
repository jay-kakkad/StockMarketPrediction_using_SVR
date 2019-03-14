
import pandas as pd
import pymongo
import pandas_datareader.data as web
import json


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


def main():
    print("Tested")


if __name__ == "__main__":
    main()
