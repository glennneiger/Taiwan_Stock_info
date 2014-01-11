import os
import csv
import mongo_functions
import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
#client = pymongo.MongoClient("mongodb://192.168.1.102:27017")
db = client.Taiwan_Stock
#db.cash_flow
#db.cash_flow.insert({"test":123})
#print(db.collection_names())
#input("wit key")
db_web_path = "mongodb://www.bi-xi.com:27017"
basepath = os.getcwd()+"/result"
#for dirpath, folders, files in os.walk(basepath):
folder_list = os.listdir(basepath)
#print(folder_list[-1])  #get latesed data
lasted_data = basepath+"/%s"%folder_list[-1]
#print(lasted_data)
#for dirpath, folders, files in os.walk(lasted_data)
#print(os.listdir(lasted_data))
for folders in os.listdir(lasted_data):
    #print(folders)
    #print(os.listdir(lasted_data+"/%s"%folders))
    if folders == "cash_flow" :
        db.cash_flow
        for files in os.listdir(lasted_data+"/%s"%folders):
            #print(files)
            file_path = lasted_data+"/%s"%folders+"/%s"%files
            company_number = files[:4]
            company_name   = files[5:-4]
            file_data = open(file_path,"r").read().split("\n")
            #print(db.collection_names())
            print(company_number)
            mongo_functions.save_back_to_mongo ("Taiwan_Stock","cash_flow", {"_id":company_number}) #creat object id; use company number
            #=================================================================#
            #save cash flow table values
            #=================================================================#
            #print(file_data)
            for line in file_data:
                for item in line.split(","):
                    print(item)
                    input("wait line")
            '''     
            company = mongo_functions.get_data_from_collection_by_cond("Taiwan_Stock",folders, {"_id":company_number})
            print(len(company))
            print(company)
            if len(company) == 0 :
                mongo_functions.insert_to_mongo({"_id":company_number}, "Taiwan_Stock", folders)
            else:
                mongo_functions.update_data_of_collection("Taiwan_Stock", folders, {"_id":company_number}, {"_id":company_number})
            '''
            input("wait key")

            '''
            if company_number in db.collection_names():
                print("exist") #go update
            else: 
            #if (db.collection.find({"com_number":company_number},{"_id":1})):
                print("not exist") #crite 
                #insert new id object every time. always crite a new object
                db.cash_flow.insert({
                    "com_number" : company_number,
                    "com_name"   : company_name
                })
            print(mongo_functions.get_data_from_collection_by_cond("Taiwan_Stock", "cash_flow" , {'com_number':"4908"}))
            '''
            #input("wait key")
            '''
            db.cash_flow.findAndModify({ 
                                    'query': { "com_number": "1220"},
                                    'sort:': { 'rating': 1 },
                                    #update: { $addToSet: { com_data: 1 } },
                                    'update': { "$addToSet" : {'test':"1234"}},
                                    'upsert': 'true'
                                  } )
            '''

            #mongo_functions.insert_to_mongo(data,database, collection_name)
            #mongo_functions.update_date_of_collection(database, collection_name, cond, update_dict)
            #mongo_functions.get_data_from_collection_by_cond(database, collection, cond {'com_number':4908})

