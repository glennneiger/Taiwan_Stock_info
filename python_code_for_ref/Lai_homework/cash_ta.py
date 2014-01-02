import os
import csv



def Sort_by_year (CSV_file, record):
    #sort_data = [[] for x in range(record["file_len"])]
    sort_data = [[] for x in range(len(record["year_item"]))]
    for row in csv.DictReader(CSV_file):
        current_year = row["year"]
        index = 0 
        for year in record["year_item"]:
            if(current_year == year):
                sort_data[index].append(row)
                break
            index = index +1
    #print(sort_data[0])
    return(sort_data)

def Get_year_list(CSV_file):
    year_item = []
    not_record = 0
    file_len =0
    for row in csv.DictReader(CSV_file):
        file_len = file_len+1  
        #print(row)
        current_year = row["year"]
        not_record = 1
        if len(year_item)==0:
            year_item.append(current_year)
        for record_year in year_item:
            if(current_year == record_year):
                not_record = 0
                break
        if(not_record):
            year_item.append(current_year)
    CSV_file.seek(0)  #reset reader index
        
    return {"year_item":year_item,"file_len":file_len}

def Count_cash_td(Sort_data,record):
    print(len(Sort_data[0]))
    return 0

#================================================================================#
#================================================================================#
#================================================================================#
CSV_file = open("./all_cashta_jkz.csv", "r")
record = Get_year_list(CSV_file)
print (record)
print (record["year_item"])
print (record["file_len"])

Sort_data = Sort_by_year(CSV_file,record)
#print(Sort_data[1])
Count_cash_td(Sort_data,record)

log_file = open("./jkz.log", "w")
log_file.write("%s"%Sort_data)
log_file.close()