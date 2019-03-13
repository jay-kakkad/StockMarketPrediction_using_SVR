import newspaper
from newspaper import Article
from newspaper import news_pool
import pandas as pd
import time
from .utils import *

class Feeds:
    COLLECTION_NAME = "news_feeds"
    def retrieve(self,query={}):
        return Database().retireve_data(self.COLLECTION_NAME,query)


class MoneyControl:
    COLLECTION_NAME = "news_feeds"
    def insert_feeds(self):
        source_urls = ["https://www.moneycontrol.com/news", "https://www.moneycontrol.com/stocksmarketsindia"]

        paper = newspaper.build("https://www.moneycontrol.com/", fetch_images=False, request_timeout=3)
        feeds = []
        print(len(paper.articles))

        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                                  "source": url,
                                  "authors": feed.authors,
                                  "summary": feed.summary,
                                  "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})

class LiveMint:
    COLLECTION_NAME = "news_feeds"
    def insert_feeds(self):
        source_urls = ["https://www.livemint.com/"]

        paper = newspaper.build("https://www.livemint.com/", fetch_images=False,
                                number_threads=3, request_timeout=3)
        feeds = []
        print(len(paper.articles))

        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                                  "source": url,
                                  "authors": feed.authors,
                                  "summary": feed.summary,
                                  "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})


class FinancialExpress:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["https://www.financialexpress.com/"]

        paper = newspaper.build("https://www.financialexpress.com/", fetch_images=False,
                                number_threads=3, request_timeout=3)
        feeds = []
        print(len(paper.articles))

        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                                  "source": url,
                                  "authors": feed.authors,
                                  "summary": feed.summary,
                                  "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})


class EconomicTimes:
    COLLECTION_NAME = "news_feeds"
    def insert_feeds(self):
        source_urls = ["economictimes.indiatimes.com"]

        paper = newspaper.build("https://economictimes.indiatimes.com/", fetch_images=False,
                                number_threads=3, request_timeout=3)
        feeds = []
        print(len(paper.articles))

        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                                  "source": url,
                                  "authors": feed.authors,
                                  "summary": feed.summary,
                                  "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})

class BloombergQuint:
    COLLECTION_NAME = "news_feeds"
    def insert_feeds(self):
        source_urls = ["www.bloombergquint.com/"]

        paper = newspaper.build("https://www.bloombergquint.com/", fetch_images=False,
                                number_threads=3, request_timeout=3)
        feeds = []
        print(len(paper.articles))
        count = 0
        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                print(count)
                count +=1
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                                  "source": url,
                                  "authors": feed.authors,
                                  "summary": feed.summary,
                                  "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})

class TimesOfIndia:
    COLLECTION_NAME = "news_feeds"

    def insert_feeds(self):
        source_urls = ["https://timesofindia.indiatimes.com/india","https://timesofindia.indiatimes.com/world",
                    "https://timesofindia.indiatimes.com/business"]

        paper = newspaper.build("https://timesofindia.indiatimes.com/",fetch_images=False,
                                number_threads=3,request_timeout=3)
        feeds = []
        print(len(paper.articles))

        for article in paper.articles:
            url = article.url
            if any(source_url in url for source_url in source_urls):
                pass
            else:
                continue
            try:
                feed = Article(url, language='en', number_threads=3)
                feed.download()
                feed.parse()
                print("Parsed:" + url)
                if feed.text != "" or feed.text != None:
                    feeds.append({"published_date": feed.publish_date,
                              "source": url,
                              "authors": feed.authors,
                              "summary": feed.summary,
                              "text": feed.text})
            except Exception as e:
                print(e)

        Database().insert_data(self.COLLECTION_NAME, feeds)
        Database().delete_data(self.COLLECTION_NAME, {"text": ""})




