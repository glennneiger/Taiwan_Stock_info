import os
import math
import csv
import pymongo
import collections
#client = pymongo.MongoClient("localhost", 27017)
client = pymongo.MongoClient("mongodb://www.bi-xi.com:27017")
#client = pymongo.MongoClient("mongodb://192.168.1.102:27017")
db = client.Taiwan_Stock


#1.本益比法：每股盈餘（EPS）*14
#2.殖利率法：每股現金股利/0.06
#3.K值法：淨值*（財報公布ROE/股東期望ROE）/ 投資者要自行預估股東期望ROE

#But我覺得可以修正的部分
#本業收入比 => 70% (因為有些公司是大陸營收為主)
#本益比法：每股盈餘（EPS）* 10 一般來說台股很多都介於 8 - 12...so 10買進的風險很低 但很多權值績優股一般都介於12 - 16 so 12對那些股票較好
#所以我個人覺得最好的做法是個股平均近五年的EPS區間 取他的中間值 取平均的方式可以是
#1. 加總平均/4
#2. 幾何平均 (geometric mean) - 可以減除劇烈震盪impact
#3. Min (above two) ==> Final value
#4. so you will get one MIN and one MAX. The middle value of MIN and MAX is your condition!
#K值法：淨值*（財報公布ROE/股東期望ROE）
#鬆散: 股東期望ROE = 8 (較不會漏掉好股)
#嚴格: 股東期望ROE = 10 (會幾乎篩選不到股票 精兵政策)
#Here ROE是年為單位非四季 所以建議用最近流續四季的加總值
#Peter K值法 = 淨值*（財報公布ROE/股東期望ROE）+ ROA必須要大於2% - 4% (>4% is excellent)
#鬆散: 股東期望ROE = 8
#嚴格: 股東期望ROE = 10

Fish_result_list = open("Fish_result_list.txt", "r").read()
for com_number in Fish_result_list.split("\n"):
    print(com_number)
#===================================================================#
#     本益比法：每股盈餘（EPS）* 12
#1. 加總平均/5 years ==>   20季/20*4 
#2. 幾何平均 (geometric mean) - 可以減除劇烈震盪impact
#===================================================================# 
    EPS_list = db.quarter_revenue_no_merge.find({"_id":com_number})    
    for loop1 in EPS_list:
        EPS_month_list = loop1["稅後每股盈餘(元)"]
        print(EPS_month_list)
        if(len(EPS_month_list) < 20):
            print("\n Not enought 5 years \n")
        #===================================================================# 
        #1. 加總平均/5 years ==>   20季/20*4 
        #===================================================================# 
        EPS_sum = 0
        EPS_AVG = 0
        for loop2 in EPS_month_list[0]:
            print(loop2)
            EPS_sum = EPS_sum + float(loop2)
        EPS_AVG = EPS_sum/len(EPS_month_list[0]) * 4
        EPS_AVG_result = EPS_AVG * 12
        print("EPS_AVG_result: %f"%EPS_AVG_result)
        #===================================================================# 
        #2. 幾何平均 (geometric mean) - 可以減除劇烈震盪impact
        #===================================================================# 
        EPS_mul = 1
        EPS_GV = 0
        for loop2 in EPS_month_list[0]:
            EPS_mul = EPS_mul * float(loop2)
        print(EPS_mul)
        EPS_GV = (math.pow(EPS_mul,(1/len(EPS_month_list[0])))) * 4
        EPS_GV_result = EPS_GV * 12
        print("EPS_GV_result: %f"%EPS_GV_result)
        input("wait")












#===================================================================#
#ROE                                                                #
#===================================================================#   
balance_sheet = db.balance_sheet.find()
total_shareholder_equity =0
total_operation_income=0
ROE_com_list={}
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
                    ROE_com_list["%s"%str(com_total_data["_id"])] ="ROE:%.2f"%ROE
                    #ROE_com_list = collections.OrderedDict(sorted(ROE_com_list.items()))
                    #print(ROE_com_list)    
                    #input("wait key")
                    #print(ROE_com_list["3443"])
                    #input("wait key")
                    
ROE_com_list = collections.OrderedDict(sorted(ROE_com_list.items()))
print(ROE_com_list)    
#input("key")



