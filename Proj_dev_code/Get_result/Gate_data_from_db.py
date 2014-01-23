import os
import csv
import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
#client = pymongo.MongoClient("mongodb://192.168.1.102:27017")
db = client.Taiwan_Stock


#get_data = db.basic_information.find({"_id":"4908", "本益比.0": {"$lt":"16"} })  # $gt
basic_info_list = db.basic_information.find({"收盤價.0":{"$lt":"50"}, "本益比.0": {"$lt":"15"}})  # $gt
shareholding = db.shareholding_distribution.find ({"董監持股.0.1":{"$gt":"10"}})

basic_info_com_list = []
for loop1 in basic_info_list:  
    basic_info_com_list.append(loop1["_id"])
    
shareholding_com_list = []
for loop1 in shareholding:  
    shareholding_com_list.append(loop1["_id"])    
    
company_list =list(set(basic_info_com_list) & set(shareholding_com_list))
print(company_list) 
print("//rual 1 ======================//") 

quarter_financial_ratio_sheet = db.quarter_financial_ratio_sheet.find({
                                                                      "流動比率.0.0":{"$gt":"110"},
                                                                      "流動比率.0.1":{"$gt":"110"},
                                                                      "流動比率.0.2":{"$gt":"110"},
                                                                      "流動比率.0.3":{"$gt":"110"},
                                                                      "速動比率.0.0":{"$gt":"110"},
                                                                      "速動比率.0.1":{"$gt":"110"},
                                                                      "速動比率.0.2":{"$gt":"110"},
                                                                      "速動比率.0.3":{"$gt":"110"},
                                                                      "利息保障倍數.0.0":{"$gt":"0"},
                                                                      "利息保障倍數.0.1":{"$gt":"0"},
                                                                      "利息保障倍數.0.2":{"$gt":"0"},
                                                                      "利息保障倍數.0.3":{"$gt":"0"},
                                                                      "股東權益報酬率.0.0":{"$gt":"1"},
                                                                      "股東權益報酬率.0.1":{"$gt":"1"},
                                                                      "股東權益報酬率.0.2":{"$gt":"1"},
                                                                      "股東權益報酬率.0.3":{"$gt":"1"},
                                                                      "每股營業利益(元).0.0":{"$gt":"0"},
                                                                      "每股營業利益(元).0.1":{"$gt":"0"},
                                                                      "每股營業利益(元).0.2":{"$gt":"0"},
                                                                      "每股營業利益(元).0.3":{"$gt":"0"}
                                                                      }) 
quarter_financial_com_list = []
for loop1 in quarter_financial_ratio_sheet:  
    quarter_financial_com_list.append(loop1["_id"])  
                                                     
company_list =list(set(company_list) & set(quarter_financial_com_list))
print(company_list)

print("//rual 2 ======================//") 

quarter_dividend_merge = db.quarter_dividend_merge.find({
                                                         "合計.0.0":{"$gt":"1"},
                                                         "合計.0.1":{"$gt":"1"},
                                                         "合計.0.2":{"$gt":"1"},
                                                         "合計.0.3":{"$gt":"1"},
                                                        }) 
quarter_dividend_merge_com_list = []
for loop1 in quarter_dividend_merge:  
    quarter_dividend_merge_com_list.append(loop1["_id"])  
print("quarter_dividend_merge_com_list")
print(quarter_dividend_merge_com_list)

print("//rual 3 ======================//") 

monthly_revenue_no_merge = db.monthly_revenue_no_merge.find({
                                                         "年增率.1.0":{"$gt":"0.1"},  #0:季增， 1累計
                                                         "年增率.1.1":{"$gt":"0.1"},
                                                         "年增率.1.2":{"$gt":"0.1"},
                                                         "年增率.1.3":{"$gt":"0.1"},
                                                        }) 
monthly_revenue_no_merge_com_list = []
for loop1 in monthly_revenue_no_merge:  
    monthly_revenue_no_merge_com_list.append(loop1["_id"])  
print("monthly_revenue_no_merge")
print(monthly_revenue_no_merge_com_list)

           
company_list =list(set(company_list) & set(monthly_revenue_no_merge_com_list))
print(company_list)
input("wait")
    





'''
for loop1 in quarter_financial_ratio_sheet:
    print("loop1 "+loop1["_id"])
input("wait")
for loop1 in basic_info_list:
    print("loop1"+loop1["_id"])
input("wait")
for loop2 in shareholding:
    print("loop2"+loop2["_id"])
input("wait")


for loop1 in basic_info_list:  
    for loop2 in shareholding:    
        print("loop1"+loop1["_id"])
        print("loop2"+loop2["_id"])
        if(loop1["_id"]==loop2["_id"]):
            print(loop2["_id"])
            input("wait")  
    print("loop1"+loop1["_id"])
    print("loop2"+loop2["_id"])
    input("wait")
'''                             
