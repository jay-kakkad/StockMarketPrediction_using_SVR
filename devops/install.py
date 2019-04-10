from news_utility.feeds import *
from news_utility.utils import *
from statistical_utility.exchanges.sensex import SENSEX
from statistical_utility.exchanges.nifty50 import NIFTY
from statistical_utility.nse_stocks.sunpharma import SUNPHARMA
from statistical_utility.nse_stocks.pfizer import PFIZER
from statistical_utility.nse_stocks.drreddy import DRREDDY
from statistical_utility.nse_stocks.autoline import AUTOLINE

def get_news():
    MoneyControl().insert_feeds()
    LiveMint().insert_feeds()
    FinancialExpress().insert_feeds()
    EconomicTimes().insert_feeds()
    BloombergQuint().insert_feeds()

def redo_stocks():
    SENSEX().store_inter_day_data()
    NIFTY().store_inter_day_data()
    SUNPHARMA().store_inter_day_data()
    PFIZER().store_inter_day_data()
    DRREDDY().store_inter_day_data()

def evaluate_ti():
    SENSEX().technical_indicators()
    NIFTY().technical_indicators()
    SUNPHARMA().technical_indicators()
    PFIZER().technical_indicators()
    DRREDDY().technical_indicators ()

def get_stocks():
    SENSEX().daily_update()
    NIFTY().daily_update()
    # SUNPHARMA().daily_update()
    # PFIZER().daily_update()
    # DRREDDY().daily_update()

# NewsUtil().update_date()
if __name__ == "__main__":
    # AUTOLINE().store_inter_day_data()
    # AUTOLINE().technical_indicators()