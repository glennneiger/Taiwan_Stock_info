import pymongo
client = pymongo.MongoClient("localhost", 27017)
#client = pymongo.MongoClient("mongodb://localhost:271017/")
db = client.Taiwan_Stock
db.name
db.my_collection
db.my_collection.save({"x": 10})
db.my_collection.save({"x": 8})
db.my_collection.save({"x": 11})
db.my_collection.find_one()
for item in db.my_collection.find():
    print (item["x"])
