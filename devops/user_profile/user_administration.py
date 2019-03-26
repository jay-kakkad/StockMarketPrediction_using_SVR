import datetime as dt
from .utils import Secure,DB
import pymongo

class User:
    DB = "jsrdb"
    COLLECTION = "user_profile"
    ID = None
    FIRST_NAME = None
    LAST_NAME = None
    EMAIL = None
    PASSWORD = None
    DOB = None
    TWITTER_ID = None
    OCCUPATION = None
    COUNTRY = None
    MOBILE = None
    STATUS = None
    CACHE = None

    def __init__(self,f_name=None,l_name=None,email=None,pwd=None,
                 dob=None,twitter_id=None,occupation=None,country=None,mobile=None,status=None):
        self.FIRST_NAME = f_name
        self.LAST_NAME = l_name
        self.EMAIL = email
        self.PASSWORD = pwd
        self.DOB = dob
        self.TWITTER_ID = twitter_id
        self.OCCUPATION = occupation
        self.COUNTRY = country
        self.MOBILE = mobile
        self.STATUS = status


    def login_verification(self,email,password):
        db = DB()
        query = {"email": email, "password": password}
        result = db.DATABASE.find_one(query)
        if result != None:
            secure = Secure()
            secure.ID = secure.encrypt_data(result["_id"])
            self.CACHE = result
            db.CLIENT.close()
            return secure
        else:
            db.CLIENT.close()
            return False
        return None

    def create_user(self):
        db = DB()
        query = {"email" : self.EMAIL}
        result = db.DATABASE.find_one(query)
        if result == None:
            data_format = {"first_name": self.FIRST_NAME,"last_name": self.LAST_NAME,"email": self.EMAIL,
                           "password": self.PASSWORD,"date_of_birth": self.DOB,
                           "twitter_id": self.TWITTER_ID,"occupation": self.OCCUPATION,
                           "country": self.COUNTRY,"mobile": self.MOBILE,"status": self.STATUS}
            db.DATABASE.insert_one(data_format)
            return True
        else:
            db.CLIENT.close()
            return False
        return None

    def del_user(self):
        db = DB()
        query = {"email": self.CACHE["email"]}
        result = db.DATABASE.delete_one(query)
        verify = db.DATABASE.find_one(query)
        if verify != None:
            db.close_db()
            return False
        else:
            db.close_db()
            return True
        return None

    def update_user(self,f_name=None,l_name=None,pwd=None,dob=None,
                    twitter_id=None,occupation=None,country=None,mobile=None,status=None):
        db = DB()
        self.CACHE["first_name"] = f_name if f_name != None else self.CACHE["first_name"]
        self.CACHE["last_name"] = l_name if l_name != None else self.CACHE["last_name"]
        self.CACHE["password"] = pwd if pwd != None else self.CACHE["password"]
        self.CACHE["date_of_birth"] = dob if dob != None else self.CACHE["date_of_birth"]
        self.CACHE["twitter_id"] = twitter_id if twitter_id != None else self.CACHE["twitter_id"]
        self.CACHE["occupation"] = occupation if occupation != None else self.CACHE["occupation"]
        self.CACHE["country"] = country if country != None else self.CACHE["country"]
        self.CACHE["mobile"] = mobile if mobile != None else self.CACHE["mobile"]
        self.CACHE["status"] = status if status != None else self.CACHE["status"]
        query = {"email": self.CACHE["email"]}
        new_values = {"$set": self.CACHE}
        db.DATABASE.update_one(query,new_values)
        db.close_db()
        return None


    # def initialize_db(self):
    #     return pymongo.MongoClient("mongodb://localhost:27017/")


if __name__ == "__main__":
    user = User()
    x = User(f_name="admin", email="admin2@somaiya.edu", pwd="admin")
    login = user.login_verification("admin@somaiya.edu","admin")
    # print(x.PASSWORD)
    #
    user.update_user(occupation="admin")

