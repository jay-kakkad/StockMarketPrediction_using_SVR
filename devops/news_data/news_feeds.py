import newspaper
from newspaper import Article
import pandas as pd
from .utils import *

class MoneyControl:
    COLLECTION_NAME = "news_feeds"
    # LABELS = {"business","business/markets","business/stocks","business/economy","business/ipo","politics","india","world","bfsi-tech","technology"}
    URL = 'https://www.moneycontrol.com/'

    def insert_feeds(self):
        feeds = []
        paper = newspaper.build(self.URL)
        print(len(paper.articles))
        # for article in paper.articles:
        #     url = article.url
        #     feed = Article(url)
        #     print(feed.summary)
            # feeds.append({"published_date":feed.publish_date,
            #                 "source":url,
            #                 "authors":feed.authors,
            #                 "summary":feed.summary,
            #                 "text":feed.text})
        # Database().insert_data(self.COLLECTION_NAME,feeds)




class LiveMint:
    COLLECTION_NAME = "news_feeds"
    def daily_update_data(self):
        paper = newspaper.build("https://www.livemint.com/")


class FinancialExpress:
    COLLECTION_NAME = "news_feeds"
    def daily_update_data(self):
        paper = newspaper.build("https://www.financialexpress.com/")


class EconomicTimes:
    COLLECTION_NAME = "news_feeds"
    def daily_update_data(self):
        paper = newspaper.build("https://economictimes.indiatimes.com/")


class TimesOfIndia:
    COLLECTION_NAME = "news_feeds"
    def daily_update_data(self):
        paper = newspaper.build("https://timesofindia.indiatimes.com/")




