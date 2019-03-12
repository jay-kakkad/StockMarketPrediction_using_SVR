from .utils import Database
import datetime as dt


class DRREDDY:
    STOCK = 'DRREDDY.NS'
    SOURCE = 'yahoo'
    COLLECTION_NAME = 'drreddy_ns_'

    def store_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        start = dt.datetime(2000,1,1)
        end = dt.datetime.now()
        return Database().update_inter_day_data(self.STOCK, self.SOURCE, start, end, collection_name)

    def retrieve_inter_day_data(self, start, end):
        collection_name = self.COLLECTION_NAME + ".inter_day_values"
        # print(str(start))
        query = {"Date": {'$gte': str(start), '$lt': str(end)}}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_inter_day_data(self, date):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        # print(str(start))
        query = {"Date": date}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        query = {}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def daily_update(self):
        today = dt.date.today()
        print(today)
        records = DRREDDY().retrieve_inter_day_data()
        last_working_day = dt.datetime.strptime(records["Date"].iloc[-1], "%Y-%m-%d").date()
        print(last_working_day)
        if today > last_working_day  and today.weekday() < 5:
            last_working_day = last_working_day + dt.timedelta(days=1)
            collection_name = self.COLLECTION_NAME + "inter_day_values"
            return Database().update_inter_day_data(self.STOCK, self.SOURCE, last_working_day, today, collection_name)
        elif today == last_working_day or today.weekday() >= 5:
            print("Data Up to Date")
            return None
        else:
            print("Recheck DB")
            return None

    def moving_average(self,window_size):
        df = DRREDDY().retrieve_inter_day_data()
        ma = df["Close"].rolling(window=window_size).mean()
        return ma

    def exponential_moving_average(self,windows_size):
        df = DRREDDY().retrieve_inter_day_data()
        ema = df["Close"].ewm(span=windows_size, adjust=False)
        return ema

    def volume_weighted_average_price(self):
        df = DRREDDY().retrieve_inter_day_data()
        q = df["Close"]
        p = df["Volume"]
        vmap = (p * q).cumsum() / q.cumsum()
        return vmap


def initialize_app():
    return DRREDDY()


if __name__ == "__main__":
    DRREDDY().store_inter_day_data()
    # DRREDDY().retrieve_inter_day_data(dt.datetime(2018,5,1).strftime('%Y-%m-%d'),dt.datetime.today().strftime('%Y-%m-%d'))
    # DRREDDY().store_inter_day_data()
    # DRREDDY().daily_update()
    # print(DRREDDY().retrieve_inter_day_data())