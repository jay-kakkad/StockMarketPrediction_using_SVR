from .utils import Database,Technical_Indicators
import datetime as dt
import pandas as pd


class DRREDDY:
    STOCK = 'DRREDDY.NS'
    SOURCE = 'yahoo'
    COLLECTION_NAME = 'drreddy_ns_'

    def store_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        start = dt.datetime(2000,1,1)
        end = dt.datetime.now()
        return Database().inter_day_data(self.STOCK, self.SOURCE, start, end, collection_name)

    def retrieve_inter_day_data(self, start, end):
        collection_name = self.COLLECTION_NAME + ".inter_day_values"
        query = {"Date": {'$gte': str(start), '$lt': str(end)}}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_inter_day_data(self, date):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        query = {"Date": date}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_inter_day_data(self):
        collection_name = self.COLLECTION_NAME + "inter_day_values"
        query = {}
        records = Database().retireve_data(collection_name, query)
        return records[['_id', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    def retrieve_ti(self):
        query = {}
        records = Database().retireve_data(self.COLLECTION_NAME + "ti", query)
        return records

    def daily_update(self):
        today = dt.date.today()
        print(today)
        records = DRREDDY().retrieve_inter_day_data()
        last_working_day = dt.datetime.strptime(records["Date"].iloc[-1], "%Y-%m-%d").date()
        print(str(last_working_day))
        if today > last_working_day  and today.weekday() < 5:
            last_working_day = last_working_day + dt.timedelta(days=1)
            collection_name = self.COLLECTION_NAME + "inter_day_values"
            return Database().inter_day_data(self.STOCK, self.SOURCE, last_working_day, today, collection_name)
        elif today == last_working_day or today.weekday() >= 5:
            print("Data Up to Date")
            return None
        else:
            print("Recheck DB")
            return None

    def technical_indicators(self):
        obj = Technical_Indicators(DRREDDY())
        short_ma = obj.MA(14, obj.DF["Close"])
        long_ma = obj.MA(90, obj.DF["Close"])
        short_ema = obj.EMWA(14, obj.DF["Close"])
        long_ema = obj.EMWA(90, obj.DF["Close"])
        macd = obj.MACD(obj.DF["Close"], obj.OBJ)
        stok = obj.STOK(obj.DF["Close"], obj.DF["Low"], obj.DF["High"], 14)
        stod = obj.STOD(stok)
        rsi_6 = obj.RSI(obj.DF["Close"].diff(), 6)
        rsi_12 = obj.RSI(obj.DF["Close"].diff(), 12)
        # print(rsi_6)
        # print(type(short_ma),type(long_ma),type(short_ema),type(long_ema),type(stok),type(stod))
        result = pd.DataFrame({"Date": obj.DF["Date"], "MA_14": short_ma,
                               "MA_90": long_ma, "EMA_14": short_ema, "EMA_90": long_ema, "MACD": macd,
                               "%K": stok, "%D": stod, "RSI_6": rsi_6, "RSI_12": rsi_12})
        print(result.tail())
        Database().store_data(result, self.COLLECTION_NAME + "ti")
        return None


def initialize_app():
    return DRREDDY()


if __name__ == "__main__":
    DRREDDY().store_inter_day_data()