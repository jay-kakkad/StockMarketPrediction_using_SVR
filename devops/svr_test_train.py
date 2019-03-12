from numerical_data.nse_stocks.drreddy import DRREDDY
from numerical_data.nse_stocks.sunpharma import SUNPHARMA
from numerical_data.nse_stocks.pfizer import PFIZER
# from numerical_data.exchanges.sensex import SENSEX
# from numerical_data.exchanges.nifty50 import NIFTY
# from user_profile.user_administration import User
from news_data.news_feeds import MoneyControl

# drreddy = DRREDDY()
# sunpharma = SUNPHARMA()
# pfizer = PFIZER()
# sensex = SENSEX()
# nifty = NIFTY()
# user = User()
mc = MoneyControl()
mc.insert_feeds()
# print(user.create_user())
# print(user.login_verification("admin@somaiya.edu","admin").ID)
# drreddy.sma(20)
# sunpharma.retrieve_inter_day_data("")
# pfizer.store_historical_data()
# sensex.store_historical_data()
# nifty.store_historical_data()