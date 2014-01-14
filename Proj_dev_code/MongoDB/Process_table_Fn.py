import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
db = client.Taiwan_Stock

def creat_company_db(collection_name,company_number,company_name,file_data):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    for row in file_data[:-1]:
        if row != "" :
            print(row)
            items = row.split(",")
            db[collection_name].update(
                {"_id":company_number}, #find target
                {"$push" :{items[0]:items[1:-1]}}  #late item is empty; update target
                #{upsert:True}
            )        
    return 0
    
def updata_company_db(collection_name,company_number,company_name,file_data):
    #input("wait key update")
    return 0
