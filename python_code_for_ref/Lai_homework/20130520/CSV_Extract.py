import os
import csv
from CSV_filert_empty import *

#company_list = []
#previousl_com = "deadbeff"
#list_number = 1
#print(previousl_com)
def Get_company_list(CSV_file):
    previousl_com = "deadbeff"
    list_number = 1
    company_list = []
    retrun_company_list = [] 
    for row in csv.DictReader(CSV_file):  
        #print (row["本期稅後淨利"])
        #print(row)
        #print (row["公司"])
        current_com = row["公司"]
        if(current_com != previousl_com):
            company_list.append(list_number)
            list_number = 1
        else:
            list_number = list_number +1    
        previousl_com = current_com
        #print (current_com)
        #print (company_list)
    #for item in range(1,len(company_list)):
    #    retrun_company_list.append(company_list[item]) #del first company number
    company_list.append(list_number) #the last nunmber
    CSV_file.seek(0)  #reset reader index
    return(company_list)

def Operate_append(Target,CSV_file, CSV_Output_file):
    #print("\"%s\""%Target)
    #for row in csv.DictReader(CSV_file,["\"%s\""%Target]):  
    index=0
    CSV_Output_file[index].append(Target)
    index=1
    for row in csv.DictReader(CSV_file):  
        CSV_Output_file[index].append(row[Target])
        index = index+1
        #print(index)
        #print(row)
    CSV_file.seek(0)  #reset reader index
    return 0

def Operate_Sub(Target,Result_name, Sub_year, COM_list, COM_list_number, CSV_file, CSV_Output_file): #  
    index=0
    Orignal_Data_var = []
    Result_Data_var =[]
    #get data
    for row in csv.DictReader(CSV_file):  
        Orignal_Data_var.append(row[Target])
    #print(len(Orignal_Data_var))
    
    #operation sub
    list_index = 1
    for company in COM_list:
        if((company==1) & (list_index == 1)):
            Result_Data_var.append(Result_name)
        else:
            for loop in range(company):
                if(loop<Sub_year):
                    Result_Data_var.append("NA")
                    list_index = list_index +1
                else:
                    Result_Data_var.append(int(Orignal_Data_var[list_index])-int(Orignal_Data_var[list_index-Sub_year]))
                    list_index = list_index +1
                    #print(list_index)
                    
    for item in range(COM_list_number):
        CSV_Output_file[item].append(Result_Data_var[item])
    CSV_file.seek(0)  #reset reader index
    return 0
    
def Operate_Shift(Target,Result_name, Shift_year, COM_list, COM_list_number, CSV_file, CSV_Output_file):
    index=0
    Orignal_Data_var = []
    Result_Data_var =[]
    #get data
    for row in csv.DictReader(CSV_file):  
        Orignal_Data_var.append(row[Target])
    
    #operation shift
    list_index = 1
    for company in COM_list:
        if((company==1) & (list_index == 1)):
            Result_Data_var.append(Result_name)
        else:
            for loop in range(company):
                if(loop<Shift_year):
                    Result_Data_var.append("NA")
                    list_index = list_index +1
                else:
                    Result_Data_var.append(float(Orignal_Data_var[list_index-Shift_year]))
                    list_index = list_index +1
                    #print(list_index)
                    
    for item in range(COM_list_number):
        CSV_Output_file[item].append(Result_Data_var[item])
    CSV_file.seek(0)  #reset reader index
    return 0

def Processing_CSV_FILE(dirPath,FileName):
    #global previousl_com
    #print(previousl_com)
    CSV_file = open(os.path.join(dirPath, FileName), 'r')  
   
    company_list = Get_company_list(CSV_file)
    print(company_list)
    company_list_len=0
    for number in company_list:
        company_list_len = company_list_len + number
    print(company_list_len)
    CSV_Output_file = [[] for x in range(company_list_len)]   # +1 for insert file name and length number
    #define what you want operation
    Operate_append("公司", CSV_file, CSV_Output_file)
    Operate_append("年", CSV_file, CSV_Output_file)
    Operate_append("市值(百萬元)", CSV_file, CSV_Output_file)
    Operate_Sub("市值(百萬元)","dmv1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("市值(百萬元)","dmv2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("股東權益總額", CSV_file, CSV_Output_file)
    Operate_Sub("股東權益總額","dna1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("股東權益總額","dna2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("本期稅後淨利", CSV_file, CSV_Output_file)
    Operate_Sub("本期稅後淨利","de1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("本期稅後淨利","de2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("營業費用─研究發展", CSV_file, CSV_Output_file)
    Operate_Sub("營業費用─研究發展","rd1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("營業費用─研究發展","rd2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("普通股─現金股利", CSV_file, CSV_Output_file)
    Operate_Sub("普通股─現金股利","dd1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("普通股─現金股利","dd2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("利息支出", CSV_file, CSV_Output_file)
    Operate_Sub("利息支出","di1",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_Sub("利息支出","di2",2, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("現金及約當現金", CSV_file, CSV_Output_file)
    Operate_Sub("現金及約當現金","dcash",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("資產總額", CSV_file, CSV_Output_file)
    Operate_append("固定資產", CSV_file, CSV_Output_file)
    Operate_append("ROA(C)稅前息前折舊前", CSV_file, CSV_Output_file)
    Operate_Shift("ROA(C)稅前息前折舊前","ROAP",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("十大股東持股(不含董監)%", CSV_file, CSV_Output_file)
    Operate_Shift("十大股東持股(不含董監)%","GOVP",1, company_list, company_list_len, CSV_file, CSV_Output_file)
    Operate_append("負債比率％", CSV_file, CSV_Output_file)
    Operate_append("負債總額", CSV_file, CSV_Output_file)
    Operate_append("流動負債", CSV_file, CSV_Output_file)
    Operate_append("流動資產", CSV_file, CSV_Output_file)
    
    #for further merge 
    CSV_Output_file.insert(0,(company_list_len,FileName))
    #print(CSV_Output_file)
    #Operate_Sub()
    CSV_file.close

    #===================================
    #Write back data
    #===================================
    Output_file = open("./Result_files/%s"%FileName,"w")
    for item in range(company_list_len+1):  #add file name 
        for element in range(len(CSV_Output_file[item])):
            if(element < len(CSV_Output_file[item])-1):
                Output_file.write("%s," %CSV_Output_file[item][element])
            else:
                Output_file.write("%s\n" %CSV_Output_file[item][element])
    Output_file.close()
    
    '''
    #print(len(CSV_Output_file))
    Output_file = open("./Result_files/%s"%FileName,"w")
    file_writer = csv.writer(Output_file)
    for item in range(company_list_len):
        file_writer.writerow(CSV_Output_file[item])
    Output_file.close()
    '''

    return 0
#===================================
#Get files  and Main function
#===================================
for dirPath, dirNames, fileNames in os.walk("./Source_file"):
    print (dirPath)
    for f in fileNames:
        print (os.path.join(dirPath, f))
print(dirPath)        
print(fileNames)
  
for Files_list in fileNames:
    #print(Files_list.find("csv"))
    if(Files_list.find("csv") > 0):
        csv_list = []
        print(Files_list)
        #CSV_filert_empty(dirPath,Files_list)
        Processing_CSV_FILE(dirPath,Files_list)
'''
Files_list = "23電子.csv"
print(Files_list)
Processing_CSV_FILE(dirPath,Files_list)
'''   
