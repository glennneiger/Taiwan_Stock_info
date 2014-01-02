'''
Created on 2013/5/7

@author: JKZhong
'''

import os
import re
#===================================
#Sub program files
#===================================
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
'''
def DNA_1_year(orignal_list_index, company_year_index):
    #print(orignal_list_index)
    #print(company_year_index)
    if(company_year_index<1):
        csv_list[orignal_list_index][4]="na"
    else:
        #print(csv_list[orignal_list_index-1][3])
        #print(csv_list[orignal_list_index][3])
        csv_list[orignal_list_index][4]=int(csv_list[orignal_list_index][3]) - int(csv_list[orignal_list_index-1][3])
    return 0

def DNA_2_year(orignal_list_index, company_year_index):
    #print(orignal_list_index)
    #print(company_year_index)
    if(company_year_index<2):
        csv_list[orignal_list_index][5]="na"
    else:
        #print(csv_list[orignal_list_index-1][3])
        #print(csv_list[orignal_list_index][3])
        csv_list[orignal_list_index][5]=int(csv_list[orignal_list_index][3]) - int(csv_list[orignal_list_index-2][3])
    return 0
'''

def Sub_DATA_year(orignal_list_index, company_year_index,DATA_INDEX,RESULT_INDEX,SUB_YEAR):
    if(company_year_index<SUB_YEAR):
        csv_list[orignal_list_index][RESULT_INDEX]="na"
    else:
        csv_list[orignal_list_index][RESULT_INDEX]=int(csv_list[orignal_list_index][DATA_INDEX]) - int(csv_list[orignal_list_index-SUB_YEAR][DATA_INDEX])
    return 0


def Processing_CVS_FILE(FileName):
    Input_file = open(os.path.join(dirPath, FileName),"r")
    Output_file = open("./Result_files/%s"%FileName,"w")
    print(Input_file)
    line_number  = file_len(os.path.join(dirPath, FileName))
    print(line_number)
    #element_number = len(Input_file.readline().split(","))
    #print(element_number)
    
    #===================================
    #Gate input data to list
    #===================================
    #csv_list = []
    for loop_num in range(line_number):
        #print (loop_num)
        csv_list.append(Input_file.readline().split(","))
        #print(len(csv_list[loop_num]))
    print(csv_list[7])
    #print(csv_list[2][0])
    #===================================
    #Gate company_year_num data length
    #===================================
    index_number = 1
    same_company_year_num_number = []
    for loop_num in range(len(csv_list)):
        if(loop_num < len(csv_list)-2):
            if(csv_list[loop_num][0] == csv_list[loop_num+1][0]):
                index_number = index_number +1
            else:
                #csv_list[loop_num].insert(0,index_number)
                same_company_year_num_number.append(index_number)
                index_number = 1
        elif(loop_num == len(csv_list)-1):#last one company
            same_company_year_num_number.append(index_number+1)
            print(same_company_year_num_number)
            print(loop_num)
        else:
            continue
    print(same_company_year_num_number)
    
    #===================================
    #Start processing data   #index start from 0,  last index number is last-1
    #===================================
    already_processing_com = 0
    for company_year_num in same_company_year_num_number:
        if(company_year_num<=2):
            already_processing_com = already_processing_com + company_year_num
        else:
            for company_year_num_year_compare in range(company_year_num):
                already_processing_com = already_processing_com +1
                #DNA_1_year(already_processing_com-1, company_year_num_year_compare)
                #DNA_2_year(already_processing_com-1, company_year_num_year_compare)
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 3,4,1)  #DNA1
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 3,5,2)  #DNA2
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 6,7,1)  #DE1
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 6,8,2)  #DE2
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 9,10,1)  #RD1
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 9,11,2)  #RD2
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 12,13,1)  #DD1
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 12,14,2)  #DD2
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 15,16,1)  #DI1
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 15,17,2)  #DI2
                Sub_DATA_year(already_processing_com-1, company_year_num_year_compare, 18,19,1)  #DCASH
    
                print(csv_list[already_processing_com-1])
            #print(csv_list[already_processing_com-1][1])
    #===================================
    #Write back data
    #===================================
    for item in range(line_number):
        for element in range(len(csv_list[item])):
            if(element < len(csv_list[item])-1):
                Output_file.write("%s," %csv_list[item][element])
            else:
                Output_file.write("%s" %csv_list[item][element])
    Output_file.close()
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
        Processing_CVS_FILE(Files_list)
