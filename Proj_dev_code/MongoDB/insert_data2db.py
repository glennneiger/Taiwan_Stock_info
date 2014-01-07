import os
import mongo_functions
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.Taiwan_Stock

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
        for files in os.listdir(lasted_data+"/%s"%folders):
            #print(files)
            file_path = lasted_data+"/%s"%folders+"/%s"%files
            company_number = files[:4]
            company_name   = files[5:-4]
            #file_data = open(file_path,"r")
            db.cash_flow
            #print(db.collection_names())
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
            '''
            print(mongo_functions.get_data_from_collection_by_cond("Taiwan_Stock", "cash_flow" , {'com_number':"4908"}))
            print(db.cash_flow.find({"com_number":"1220"}))
            db.cash_flow.findAndModify({ 
                                    'query': { "com_number": "1220"},
                                    'sort:': { 'rating': 1 },
                                    #update: { $addToSet: { com_data: 1 } },
                                    'update': { "$addToSet" : {'test':"1234"}},
                                    'upsert': 'true'
                                  } )
            

            #mongo_functions.insert_to_mongo(data,database, collection_name)
            #mongo_functions.update_date_of_collection(database, collection_name, cond, update_dict)
            #mongo_functions.get_data_from_collection_by_cond(database, collection, cond {'com_number':4908})

