from .utils import Database
import datetime as dt


class NIFTY:
    STOCK = '^NSEI'
    SOURCE = 'yahoo'
    COLLECTION_NAME = 'nifty_'

    def store_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        start = dt.datetime(2000,1,1)
        end = dt.datetime.now()
        return Database().update_inter_day_data(self.STOCK, self.SOURCE, start, end, collection_name)

    def retrieve_inter_day_data(self, start, end):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        # print(str(start))
        query = {"Date": {'$gte': str(start), '$lt': str(end)}}
        records = Database().retireve_data(collection_name, query)
        return records[['_id','Date','Open','High','Low','Close','Adj Close', 'Volume']]

    def retrieve_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        # print(str(start))
        query = {}
        records = Database().retireve_data(collection_name, query)
        return records[['_id','Date','Open','High','Low','Close','Adj Close', 'Volume']]

    def daily_update(self):
        today = dt.date.today()
        print(today.weekday())
        records = NIFTY().retrieve_inter_day_data()
        last_working_day = dt.datetime.strptime(records["Date"].iloc[-1],"%Y-%m-%d").date()
        print(type(last_working_day))
        if today > last_working_day and today.weekday()<5:
            last_working_day = last_working_day + dt.timedelta(days=1)
            collection_name = self.COLLECTION_NAME + "inter_day_values"
            return Database().update_inter_day_data(self.STOCK, self.SOURCE, last_working_day, today, collection_name)
        elif today == last_working_day or today.weekday()>=5:
            print("Data Up to Date")
            return None
        else:
            print("Recheck DB")


if __name__ == "__main__":
    # NIFTY().store_inter_day_data()
    # print(NIFTY().retrieve_inter_day_data())
    NIFTY().daily_update()
