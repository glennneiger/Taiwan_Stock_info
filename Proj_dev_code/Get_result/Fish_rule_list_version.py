import os
import csv
import pymongo
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
#client = pymongo.MongoClient("mongodb://192.168.1.102:27017")
db = client.Taiwan_Stock

#ROE  > 0
#ROA
#ROE＞8%
#營益率＞0%
#本業收入比＞80%
#利息保障倍數＞40
#自由現金流量＞0
'''
quarter_financial_ratio_sheet = db.quarter_financial_ratio_sheet.find() 
for com_total_data in quarter_financial_ratio_sheet:
    print(com_total_data)
    input("wait")
'''

#===================================================================#
#ROE                                                                #
#===================================================================#   
balance_sheet = db.balance_sheet.find()
total_shareholder_equity =0
total_operation_income=0
ROE_com_list=[[]]
ROE=0
i=0
for com_total_data in balance_sheet:
    total_shareholder_equity =0
    total_operation_income=0
    i=0
    ROE=0    
    #print(com_total_data["_id"])
    #print(com_total_data)
    pure_make_cash = db.quarter_income_sheet.find_one({"_id":com_total_data["_id"]})        
    #print(pure_make_cash)
    if(pure_make_cash != None and com_total_data != None):
        if(len(com_total_data["股東權益總額"][0])>3 and len(pure_make_cash["本期稅後淨利"][0])>3):
            for i in range(4):
                if(com_total_data["股東權益總額"][0][i] == "N/A" or pure_make_cash["本期稅後淨利"][0][i] == "N/A") :
                    break
                else:
                    total_shareholder_equity = total_shareholder_equity + int(com_total_data["股東權益總額"][0][i])
                    total_operation_income = total_operation_income + int(pure_make_cash["本期稅後淨利"][0][i])                    
            if(i==3):
                ROE = (total_operation_income / (total_shareholder_equity /4))*100
                #print(com_total_data["_id"])
                #print(ROE)    
                #input("key")    
                if(ROE > 8):
                    ROE_com_list.append([str(com_total_data["_id"]),"ROE:%.2f"%ROE])
                    ROE_com_list.sort()
                    #print(ROE_com_list)    
                    #input("wait key")

ROE_com_list.sort()
print(ROE_com_list)    
#input("key")

#===================================================================#   
#營益率＞0%
#利息保障倍數＞40
#===================================================================# 

#quarter_financial_ratio_sheet = db.quarter_financial_ratio_sheet.find({
#                                                                      "利息保障倍數.0.0":{"$gt":"40"},
#                                                                      "利息保障倍數.0.1":{"$gt":"40"},
#                                                                      "利息保障倍數.0.2":{"$gt":"40"},
#                                                                      "利息保障倍數.0.3":{"$gt":"40"},
#                                                                      "營業利益率.0.0":{"$gt":"0"},
#                                                                      "營業利益率.0.1":{"$gt":"0"},
#                                                                      "營業利益率.0.2":{"$gt":"0"},
#                                                                      "營業利益率.0.3":{"$gt":"0"}
#                                                                      })
#quarter_financial_com_list = []
#for loop1 in quarter_financial_ratio_sheet:  
#    #print(loop1)
#    #input("wait")
#    quarter_financial_com_list.append(loop1["_id"])
#print(quarter_financial_com_list)

quarter_financial_ratio_sheet = db.quarter_financial_ratio_sheet.find()
quarter_financial_com_list = [[]]
for com_total_data in quarter_financial_ratio_sheet:    
    try:
        if(int(float(com_total_data["利息保障倍數"][0][0])) > 40 and 
           int(float(com_total_data["利息保障倍數"][0][1])) > 40 and 
           int(float(com_total_data["利息保障倍數"][0][2])) > 40 and 
           int(float(com_total_data["利息保障倍數"][0][3])) > 40 and 
           int(float(com_total_data["營業利益率"][0][0])) > 0 and 
           int(float(com_total_data["營業利益率"][0][1])) > 0 and 
           int(float(com_total_data["營業利益率"][0][2])) > 0 and 
           int(float(com_total_data["營業利益率"][0][3])) > 0 ):
            quarter_financial_com_list.append([com_total_data["_id"],
                                               "利息保障倍數:%.2f"%float(com_total_data["利息保障倍數"][0][0]),
                                               "營業利益率:%.2f"%float(com_total_data["營業利益率"][0][0])
                                               ]) 
            #print(com_total_data["_id"])            
            #quarter_financial_com_list.sort()
            ##print(quarter_financial_com_list)
    except:
        pass
        #print("error")
        #print(com_total_data["_id"])
        #input("wait key")
            
quarter_financial_com_list.sort()
print(quarter_financial_com_list)

#===================================================================#
#自由現金流量＞0                                                     #
#===================================================================#    
operation_cash=0
investment_cash=0
free_cash=0
free_cash_list = [[]]
i=0
cash_flow_sheet = db.cash_flow.find()
for com_total_data in cash_flow_sheet:    
    operation_cash=0
    investment_cash=0
    free_cash=0
    i=0 
    if(cash_flow_sheet != None):
        if(len(com_total_data["來自營運之現金流量"][0])>3 and len(com_total_data["投資活動之現金流量"][0])>3):
            for i in range(4):
                if(com_total_data["來自營運之現金流量"][0][i] == "N/A" or com_total_data["投資活動之現金流量"][0][i] == "N/A") :
                    break
                else:
                    operation_cash = operation_cash + int(com_total_data["來自營運之現金流量"][0][i])
                    investment_cash = investment_cash + int(com_total_data["投資活動之現金流量"][0][i])
            if(i==3):
                free_cash = operation_cash + investment_cash    
                #print(com_total_data["_id"])
                #print(free_cash)
                #input("wait")
                if(free_cash>0):
                    free_cash_list.append([com_total_data["_id"],
                                           "Free_cash: %d"%free_cash
                                          ])
                                          
                    #free_cash_list.sort()             
                    #print(free_cash_list)  

free_cash_list.sort()             
print(free_cash_list)  
#input("key")

#===================================================================#
#本業收入比＞80%      本業獲利率（本業收入比）＝營業利益／（營業利益＋業外收入）                                                         
#===================================================================#     
#營業利益
#營業外收入合計
quarter_income_sheet = db.quarter_income_sheet.find()
operation_ratio_list = [[]]
for com_total_data in quarter_income_sheet:    
    operation_income=0
    investment_income=0
    operation_ratio =0
    i=0 
    try:
        #print(com_total_data["_id"])    
        if(quarter_income_sheet != None ):
            if(len(com_total_data["營業利益"][0])>3 and len(com_total_data["營業外收入合計"][0])>3):
                for i in range(4):
                    if(com_total_data["營業利益"][0][i] == "N/A" or com_total_data["營業外收入合計"][0][i] == "N/A") :
                        break
                    else:
                        operation_income = operation_income  + int(com_total_data["營業利益"][0][i])
                        investment_income = investment_income  + int(com_total_data["營業外收入合計"][0][i])
                operation_ratio = (operation_income  / (operation_income  + investment_income ) )*100
                
                #print(com_total_data["_id"])
                #print(operation_ratio)
                #input("wait")
                if(int(operation_ratio) > 80):                    
                    operation_ratio_list.append([com_total_data["_id"],
                                                 "本業收入比:%.2f%%"%operation_ratio
                                                ])
                    #print(operation_ratio_list)
                    #input("key")
    except:
        pass
        #print("key error")
        #print(com_total_data["_id"])
        #input("wait key")
        
operation_ratio_list.sort()
print(operation_ratio_list)
#input("wait key")

#===================================================================#
# write files
#===================================================================#
Fish_result = open("Fish_result","w")
Fish_result.write("ROE_com_list \n")
for loop in ROE_com_list:
    Fish_result.write(str(loop))
Fish_result.write("quarter_financial_com_list \n")
for loop in quarter_financial_com_list:
    Fish_result.write(str(loop))
Fish_result.write("free_cash_list \n")
for loop in free_cash_list:
    Fish_result.write(str(loop))
Fish_result.write("operation_ratio_list \n")
for loop in operation_ratio_list:
    Fish_result.write(str(loop))
    
        
#===================================================================#
# Check lsit 
#===================================================================#
company_list1 =list(set(ROE_com_list) & set(quarter_financial_com_list))
company_list2 =list(set(free_cash_list) & set(operation_ratio_list))
company_list3 =list(set(company_list1) & set(company_list2))

company_list3.sort()
print("final resut")
print(company_list3) 
input("key")
    
    
    
    
    
    
    
    
Fish_result.close()

print(len(operation_ratio_list))
print(operation_ratio_list[1][0])  #com id
input("wait key")
               
