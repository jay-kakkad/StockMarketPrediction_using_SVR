import newspaper
from newspaper import Article
from .utils import *

class Feeds:
    COLLECTION_NAME = "news_feeds"
    def retrieve(self,query={}):
        return Database().retireve_data(self.COLLECTION_NAME,query)

class MoneyControl:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["www.moneycontrol.com/news", "www.moneycontrol.com/stocksmarketsindia",
                       "www.moneycontrol.com/ipo","www.moneycontrol.com/equity-research"]

        paper = newspaper.build("https://www.moneycontrol.com/", fetch_images=False, request_timeout=3,
                               memoize_articles=True)
        total_feeds_inserted = NewsUtil().fetch_feed(source_urls,paper,self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


class LiveMint:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["www.livemint.com/latest-news","www.livemint.com/mostpopular",
                       "www.livemint.com/companies","www.livemint.com/market",
                       "www.livemint.com/money","www.livemint.com/industry",
                       "www.livemint.com/politics"]

        paper = newspaper.build("https://www.livemint.com/", fetch_images=False,
                                number_threads=3, request_timeout=3,memoize_articles=True)
        total_feeds_inserted = NewsUtil().fetch_feed(source_urls, paper, self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


class FinancialExpress:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["www.financialexpress.com/market","www.financialexpress.com/market/stocck-market",
                       "www.financialexpress.com/economy","www.financialexpress.com/industry",
                       "www.financialexpress.com/india-news","www.financialexpress.com/infrastructure",
                       "www.financialexpress.com/budget","www.financialexpress.com/defence"]

        paper = newspaper.build("https://www.financialexpress.com/", fetch_images=False,
                                number_threads=3, request_timeout=3,memoize_articles=True)
        total_feeds_inserted = NewsUtil().fetch_feed(source_urls, paper, self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


class EconomicTimes:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["economictimes.indiatimes.com/markets","economictimes.indiatimes.com/markets/stocks",
                       "economictimes.indiatimes.com/headlines.cms","economictimes.indiatimes.com/industry",
                       "prime.economictimes.indiatimes.com/news","economictimes.indiatimes.com/news"]
        paper = newspaper.build("https://economictimes.indiatimes.com/", fetch_images=False,
                                number_threads=3, request_timeout=3,memoize_articles=True)

        total_feeds_inserted = NewsUtil().fetch_feed(source_urls, paper, self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


class BloombergQuint:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["www.bloombergquint.com/markets","www.bloombergquint.com/business",
                        "www.bloombergquint.com/law-and-policy","www.bloombergquint.com/global-economics",
                        "www.bloombergquint.com/news-releases","www.bloombergquint.com/stock",
                        "www.bloombergquint.com/portfolio","www.bloombergquint.com/news",
                        "www.bloombergquint.com/bq-blue-exclusive","www.bloombergquint.com/technology",
                        "www.bloomberg.com/news","www.business-standard.com/article"]
        paper = newspaper.build("https://www.bloombergquint.com/", fetch_images=False,
                                number_threads=3, request_timeout=3, memoize_articles=True)
        total_feeds_inserted = NewsUtil().fetch_feed(source_urls, paper, self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


class TimesOfIndia:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["https://timesofindia.indiatimes.com/india","https://timesofindia.indiatimes.com/world",
                    "https://timesofindia.indiatimes.com/business"]

        paper = newspaper.build("https://timesofindia.indiatimes.com/",fetch_images=False,
                                number_threads=3,request_timeout=3)
        total_feeds_inserted = NewsUtil().fetch_feed(source_urls, paper, self.COLLECTION_NAME)
        print("Inserted " + str(total_feeds_inserted) + " Values")


if __name__ == "__main__":
    NewsUtil().update_date()
    # MoneyControl().insert_feeds()
    # LiveMint().insert_feeds()
    # FinancialExpress().insert_feeds()
    # EconomicTimes().insert_feeds()
    # BloombergQuint().insert_feeds()






