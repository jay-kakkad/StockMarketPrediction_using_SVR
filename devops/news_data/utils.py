from newsplease import NewsPlease
from datetime import datetime
import htmldate
import pandas as pd
import pymongo

class Database:
    def insert_data(self,collection_name,feeds):
        client = Database().initialize_db()
        db = client["jsrdb"]
        try:
            db[collection_name].insert_many(feeds)
            client.close()
            return len(feeds)
        except Exception as e:
            print(str(e))
            return 0


    def retireve_data(self,collection_name,query):
        client = Database().initialize_db()
        db = client["jsrdb"]
        result = list(db[collection_name].find(query))
        result = pd.DataFrame(result)
        # print(result)
        client.close()
        return result


    def delete_data(self,collection_name,query):
        client = Database().initialize_db()
        db = client["jsrdb"]
        db[collection_name].delete_many(query)
        search = db[collection_name].find(query)
        if search == None:
            return True
        else:
            return False

    def update_data(self,collection_name,update_query,update_value):
        client = Database().initialize_db()
        db = client["jsrdb"]
        db[collection_name].update_one(update_query,update_value)
        client.close()
        return None

    def initialize_db(self):
        return pymongo.MongoClient("mongodb+srv://jsr:root@cluster0-10kli.gcp.mongodb.net/test?retryWrites=true")

    def main(self):
        print("Tested")


class NewsUtil:

    def printProgressBar(self,iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
        # Print New Line on Complete
        if iteration == total:
            print()

    def fetch_feed(self,source_urls,paper,collection_name):
        feeds = []
        count = 0
        l = len(paper.articles)
        print("Total Urls:"+str(len(paper.articles)))
        if len(paper.articles)== 0:
            return 0
        NewsUtil().printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for article in  paper.articles:
            if any(source_url in article.url for source_url in source_urls):
                pass
            else:
                count = count + 1
                NewsUtil().printProgressBar(count, l, prefix='Progress:', suffix='Complete', length=50)
                continue
            try:
                article = NewsPlease.from_url(article.url)
                date = htmldate.find_date(article.url)
                title = article.title
                description = article.description
                text = article.text
                if text != "" or text != None or description!=None or title!=None:
                    feed = {"published_date": date,
                                  "title": title,
                                  "source": article.url,
                                  "description": description,
                                  "text": text}
                    feeds.append(feed)

            except Exception as e:
                print(e)
            count = count + 1
            NewsUtil().printProgressBar(count, l, prefix='Progress:', suffix='Complete', length=50)
        total_feeds_inserted=Database().insert_data(collection_name, feeds)
        Database().delete_data(collection_name, {"text": ""})
        return total_feeds_inserted

    def update_date(self):
        query = {"published_date":""}
        result=Database().retireve_data("news_feeds",query)
        print(result)
        for index,row in result.iterrows():
            print(row)
            row["published_date"]=htmldate.find_date(row["source"])
            update_query={"source":row["source"]}
            update_value={"$set": {"published_date": row["published_date"]}}
            Database().update_data("news_feeds",update_query,update_value)
            print("New Date",str(row["published_date"]))
        print(len(result))

    def delete_misfit_date(self):
        query = {"description":None}
        Database().delete_data("news_feeds",query)


    def retrieve_feeds(self,query):
        return None


if __name__ == "__main__":
    Database().main()
