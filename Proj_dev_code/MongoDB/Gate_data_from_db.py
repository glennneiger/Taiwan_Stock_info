import os
import csv
import mongo_functions
import Cash_Flow_Fn
import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
#client = pymongo.MongoClient("mongodb://192.168.1.102:27017")
db = client.Taiwan_Stock

get_data = db.cash_flow.find({"_id":"4908", "期別":["102.3Q"]})
print(get_data)
for data in get_data:
    print(data)

                             
