from news_data.feeds import *
from news_data.utils import *
from numerical_data.exchanges.sensex import SENSEX
from numerical_data.exchanges.nifty50 import NIFTY
from numerical_data.nse_stocks.sunpharma import SUNPHARMA
from numerical_data.nse_stocks.pfizer import PFIZER
from numerical_data.nse_stocks.drreddy import DRREDDY

def get_news():
    MoneyControl().insert_feeds()
    LiveMint().insert_feeds()
    FinancialExpress().insert_feeds()
    EconomicTimes().insert_feeds()
    BloombergQuint().insert_feeds()

def get_stocks():
    SENSEX().daily_update()
    NIFTY().daily_update()
    SUNPHARMA().daily_update()
    PFIZER().daily_update()
    DRREDDY().daily_update()

# NewsUtil().update_date()
if __name__ == "__main__":
    get_news()