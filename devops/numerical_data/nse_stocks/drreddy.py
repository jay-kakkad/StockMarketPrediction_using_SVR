from utils import *
import datetime as dt


class DRREDDY:
    STOCK = 'DRREDDY.NS'
    SOURCE = 'yahoo'
    COLLECTION_NAME = 'drreddy_ns_'

    def store_historical_data(self):
        collection_name = self.COLLECTION_NAME + "historical_values"
        start = dt.datetime(2000,1,1)
        end = dt.datetime.now()
        return update_historical_data(self.STOCK, self.SOURCE, start, end, collection_name)

    def retrieve_historical_data(self, start, end):
        collection_name = self.COLLECTION_NAME + ".historical_values"
        print(str(start))
        query = {"Date": {'$gte': str(start), '$lt': str(end)}}
        records = retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_historical_data(self, date):
        collection_name = self.COLLECTION_NAME + "historical_values"
        # print(str(start))
        query = {"Date": date}
        records = retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_historical_data(self):
        collection_name = self.COLLECTION_NAME + "historical_values"
        # print(str(start))
        query = {}
        records = retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def daily_update(self):
        today = dt.date.today()
        print(today)
        records = DRREDDY().retrieve_historical_data()
        last_working_day = dt.datetime.strptime(records["Date"].iloc[-1], "%Y-%m-%d").date()
        print(last_working_day)
        if today > last_working_day  and today.weekday() < 5:
            last_working_day = last_working_day + dt.timedelta(days=1)
            collection_name = self.COLLECTION_NAME + "historical_values"
            return update_historical_data(self.STOCK, self.SOURCE, last_working_day, today, collection_name)
        elif today == last_working_day or today.weekday() >= 5:
            print("Data Up to Date")
            return None
        else:
            print("Recheck DB")


if __name__ == "__main__":
    # DRREDDY().retrieve_historical_data(dt.datetime(2018,5,1).strftime('%Y-%m-%d'),dt.datetime.today().strftime('%Y-%m-%d'))
    # DRREDDY().store_historical_data()
    # DRREDDY().daily_update()
    print(DRREDDY().retrieve_historical_data())