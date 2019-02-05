import requests
# import csv
import datetime
import time
from random import randint

class AlphaVantageAPI:
	
	def __init__(self):
		print("Hello")
		
	def setCount():
		return None
	
	def setKey():
		return None

	def getKey(self):
		self.keys = open("alphaVantageKeys.txt","r").read().split(",")
		self.keys = self.keys
		return self.keys
		# return self.api_key[randint(0,2)]

if __name__ == "__main__":
	p1 = AlphaVantageAPI()
	print(p1.getKey())
