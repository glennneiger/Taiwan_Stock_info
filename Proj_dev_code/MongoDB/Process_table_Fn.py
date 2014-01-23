import csv
import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
db = client.Taiwan_Stock

#==========================================================#
#Format1 #
#==========================================================#
def Format1_creat_company_db(collection_name,company_number,company_name,file_data):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    for row in file_data[:-1]:
        if row != "" :
            #print(row)
            items = row.split(",")
            db[collection_name].update(
                {"_id":company_number}, #find target
                {"$push" :{items[0]:items[1:-1]}}  #late item is empty; update target
                #{upsert:True}
            )        
    return 0
    
def Format1_updata_company_db(collection_name,company_number,company_name,file_data):
    #input("wait key update")
    return 0
#==========================================================#
#Format2 #
#==========================================================#
def Format2_creat_company_db(collection_name,company_number,company_name,file_data,file_path):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    #for row in csv.DictReader(file_data):
    num_lines = sum(1 for line in open(file_path))
    item_number = len(file_data[0].split(",")) - 1    #skip late enpty item
    temp_data = [[None for x in range(num_lines)] for y in range(item_number)]    
    #print(temp_data)
    #input("wait input")
    i=0
    j=0
    for row in file_data:
        if row != "" :        
            row = row.replace("%","")
            j=0
            for item in row.split(","):
                if item !="":
                    #print(item)
                    temp_data[j][i] = item
                    j=j+1
            #print(row)
            #print(temp_data)
            #input("wait key")
            i=i+1
            
    for line_data in temp_data:
        #print(line_data)
        db[collection_name].update(
            {"_id":company_number}, #find target
            {"$push" :{line_data[0]:line_data[1:-1]}}  #late item is empty; update target
            #{upsert:True}
        )        
        #input ("wait key")        
    return 0
    
def Format2_updata_company_db(collection_name,company_number,company_name,file_data,file_path):
    #input("wait key update")
    return 0     
    
#==========================================================#
#Format3 #
#==========================================================#
def Format3_creat_company_db(collection_name,company_number,company_name,file_data):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    for row in file_data[:-1]:
        if ( (row != "") & (len(row.split(","))>2)):
            #print(row)
            items = row.split(",")
            db[collection_name].update(
                {"_id":company_number}, #find target
                {"$push" :{items[0]:items[1:-1]}}  #late item is empty; update target
                #{upsert:True}
            )        
    return 0
    
def Format3_updata_company_db(collection_name,company_number,company_name,file_data):
    #input("wait key update")
    return 0
    
#==========================================================#
#Format4 #
#==========================================================#
def Format4_creat_company_db(collection_name,company_number,company_name,file_data):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    for row in file_data[:-1]:
        if (row != ""):
            row = row.replace("%","")
            #print(row)
            items = row.split(",")
            if (items[0]!=""):
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[0]:items[1:-1]}}  #late item is empty; update target
                    #{upsert:True}
                )        
    return 0
    
def Format4_updata_company_db(collection_name,company_number,company_name,file_data):
    #input("wait key update")
    return 0
    
    
#==========================================================#
#Format5 #
#==========================================================#
def Format5_creat_company_db(collection_name,company_number,company_name,file_data):
    db[collection_name].insert({        #creat company object
        "_id":company_number,
        "com_name":company_name,
    })
    i=1
    for row in file_data[:-1]:        
        if (row != ""):
            items = row.split(",")
            if(i==1 or i==3):    
                #print(row)      
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[0]:items[1]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[2]:items[3]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[4]:items[5]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[6]:items[7]}}  #late item is empty; update target
                )        
            if(i==2 or i==4 or i==5 or i==7 or i==8):
                #print(row)      
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[0]:items[1]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[2]:items[3]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[4]:items[5]}}  #late item is empty; update target
                )        
            if(i==9 or i==10 or i==11):
                #print(row)      
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[0]:items[1]}}  #late item is empty; update target
                )        
                db[collection_name].update(
                    {"_id":company_number}, #find target
                    {"$push" :{items[2]:items[3]}}  #late item is empty; update target
                )        
        i=i+1 #next row
    return 0
    
def Format5_updata_company_db(collection_name,company_number,company_name,file_data):
    #input("wait key update")
    return 0
    
    
    
    
