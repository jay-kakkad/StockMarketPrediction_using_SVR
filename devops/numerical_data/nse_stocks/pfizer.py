from utils import *
import datetime as dt


class PFIZER:
    STOCK = 'PFIZER.NS'
    SOURCE = 'yahoo'
    COLLECTION_NAME = 'pfizer_ns_'

    def initial_store_historical_data(self):
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
        # print(today)
        records = PFIZER().retrieve_historical_data()
        last_working_day = dt.datetime.strptime(records["Date"].iloc[-1],"%Y-%m-%d").date()
        # print(type(last_working_day))
        if today > last_working_day and today.weekday() < 5:
            last_working_day = last_working_day + dt.timedelta(days=1)
            collection_name = self.COLLECTION_NAME + "historical_values"
            return update_historical_data(self.STOCK, self.SOURCE, last_working_day, today, collection_name)
        elif today == last_working_day or today.weekday() >= 5:
            print("Data Up to Date")
            return None
        else:
            print("Recheck DB")

    def update_historical_data(self):
        collection_name = self.COLLECTION_NAME + "historical_values"
        return None

    def delete_historical_data(self):
        return None

    def check_deduplication(self):
        return None

if __name__ == "__main__":
    # PFIZER().initial_store_historical_data()
    PFIZER().daily_update()