from cryptography.fernet import Fernet
import pymongo


class Secure:
    KEY = Fernet.generate_key()
    cipher_suite = Fernet(KEY)
    ID = None
    def encrypt_data(self,data):
        return self.cipher_suite.encrypt(str(data).encode())

    def decrypt_date(self,data):
        return self.cipher_suite.decrypt(data)


class DB:
    DB_Name = "jsrdb"
    COLLECTION_Name = "user_profile"
    CLIENT = None
    DATABASE = None

    def __init__(self):
         self.CLIENT = pymongo.MongoClient("mongodb+srv://jsr:root@cluster0-10kli.gcp.mongodb.net/test?retryWrites=true")
         self.DATABASE =  self.CLIENT[self.DB_Name][self.COLLECTION_Name]

    def close_db(self):
        return self.CLIENT.close()



