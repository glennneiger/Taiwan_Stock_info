import os
import csv
import mongo_functions
import Process_table_Fn
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
    
    
    #=============================================================================#
    #below data table are same as cash_flow table; use cash flow functions        #
    #=============================================================================#
    
    if folders == "cash_flow" :
        db.cash_flow
        for files in os.listdir(lasted_data+"/%s"%folders):
            #print(files)
            file_path = lasted_data+"/%s"%folders+"/%s"%files            
            file_data = open(file_path,"r")
            company_number = files[:4]
            company_name   = files[5:-4]
            #print(db.collection_names())P
            print(company_number)
            company_exist = db.cash_flow.find({"_id":company_number}).count()
            if company_exist !=0 : #updata
                Process_table_Fn.updata_company_db(folders,company_number,company_name,file_data.read().split("\n"))
            else : #creat 
                Process_table_Fn.creat_company_db(folders,company_number,company_name,file_data.read().split("\n"))
            file_data.close()
    
    if folders == "balance_sheet" :
        db.balance_sheet
        for files in os.listdir(lasted_data+"/%s"%folders):
            #print(files)
            file_path = lasted_data+"/%s"%folders+"/%s"%files            
            file_data = open(file_path,"r")
            company_number = files[:4]
            company_name   = files[5:-4]
            #print(db.collection_names())
            print(company_number)
            company_exist = db.balance_sheet.find({"_id":company_number}).count()
            if company_exist !=0 : #updata
                Process_table_Fn.updata_company_db(folders,company_number,company_name,file_data.read().split("\n"))
            else : #creat 
                Process_table_Fn.creat_company_db(folders,company_number,company_name,file_data.read().split("\n"))
            file_data.close()
    
