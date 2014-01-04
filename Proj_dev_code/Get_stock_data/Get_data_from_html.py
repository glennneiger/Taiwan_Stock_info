# -*- coding: utf-8 -*-
#=================================================================#
#get formal html data
#=================================================================#
def get_formal_html_data (Stock_data):
    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("Formal_data.txt", "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()
    return 0
#=================================================================#
#=================================================================#
#個股財務比率季表 cathaysec.moneydj.com/z/zc/zcr/zcr0_%s.djhtm
def company_quarter_financial_ratio_sheet  (company_number,company_name,date,basepath,folder_name):
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zcr/zcr0_%s.djhtm'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print(Stock_data)
    get_formal_html_data(Stock_data)

    #print(basepath)
    from bs4 import BeautifulSoup
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[1:-2]:
        for tr in table.findAll("tr")[2:]:  
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0
#=================================================================#
#=================================================================#
#個股損益季表 cathaysec.moneydj.com/z/zc/zcq/zcq0_%s.djhtm
def company_quarter_income_statement_sheet  (company_number,company_name,date,basepath,folder_name):
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zcq/zcq0_%s.djhtm'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print(Stock_data)
    get_formal_html_data(Stock_data)

    #print(basepath)
    from bs4 import BeautifulSoup
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[2:]:
        for tr in table.findAll("tr")[1:]:  
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0
#=================================================================#
#=================================================================#
#資產負債季表 cathaysec.moneydj.com/z/zc/zcp/zcpa/zcpa0_%s.djhtm
def company_balance_sheet  (company_number,company_name,date,basepath,folder_name):
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zcp/zcpa/zcpa0_%s.djhtm'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print(Stock_data)
    get_formal_html_data(Stock_data)

    #print(basepath)
    from bs4 import BeautifulSoup
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[2:]:
        for tr in table.findAll("tr")[1:]:  
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0
#=================================================================#
#=================================================================#
#個股現金流量季表 cathaysec.moneydj.com/z/zc/zc3/zc30_%s.djhtm
def company_cash_flow  (company_number,company_name,date,basepath,folder_name):
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zc3/zc30_%s.djhtm'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print(Stock_data)
    get_formal_html_data(Stock_data)

    #print(basepath)
    from bs4 import BeautifulSoup
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[2:]:
        for tr in table.findAll("tr")[1:-1]:  
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0
#=================================================================#
#=================================================================#
#Distribution of shareholding
#籌碼分佈  cathaysec.moneydj.com/z/zc/zcx/zcxD1.djjs?A=%s
def company_shareholding_distribution (company_number,company_name,date,basepath,folder_name):
    # get html data
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zcx/zcxD1.djhtm?A=%s'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print (Stock_data)

    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("Formal_data.txt", "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()
    
    #print(basepath)
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table"):
        for tr in table.findAll("tr")[1:]:
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0

#=================================================================#
#=================================================================#
#個股速覽 cathaysec.moneydj.com/Z/ZC/ZCX/ZCXNEWCATHAYSEC.DJHTM?A=%s
def company_information (company_number,company_name,date,basepath,folder_name):
    # get html data
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/Z/ZC/ZCX/ZCXNEWCATHAYSEC.DJHTM?A=%s'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print (Stock_data)
    #input("press a key")
    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("Formal_data.txt", "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()

    #print(basepath)
    directory = basepath+"/%s/%s/"%(date,folder_name)
    #print(basepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[2:-3]:
        for tr in table.findAll("tr")[1:]:
            for td in tr.findAll("td"):
                td_result = td.text.replace('\n','') #remove change line
                td_result = td_result.replace(' ','') #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    
    return 0

#=================================================================#
#=================================================================#
#每年股利，合併 http://cathaysec.moneydj.com/Z/ZC/ZCC/ZCC.DJHTM?A=%s
def company_quarterly_dividend_report_merge (company_number,company_name,date,basepath,folder_name):
    # get html data
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/Z/ZC/ZCC/ZCC.DJHTM?A=%s'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print (Stock_data)

    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("Formal_data.txt", "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()
    
    #print(basepath)
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top three table
    for table in stock_input_data.findAll("table")[3:]:
        for tr in table.findAll("tr"):
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0

#=================================================================#
#=================================================================#
#每季營餘，合併 http://cathaysec.moneydj.com/z/zc/zch/zcha_%d.djhtm
def company_quarterly_profit_report_merge (company_number,company_name,date,basepath,folder_name):
    # get html data
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zch/zcha_%s.djhtm'%company_number)
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print (Stock_data)

    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("Formal_data.txt", "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()
    
    #print(basepath)
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top one table and last
    for table in stock_input_data.findAll("table")[1:-1]:
        #skip top four tr
        for tr in table.findAll("tr")[4:]:
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0

#=================================================================#
#=================================================================#
#每季營收，非合併 http://cathaysec.moneydj.com/z/zc/zcd_%d_2.djhtm
#每季營收，合併   http://cathaysec.moneydj.com/z/zc/zcd_%d.djhtm
def company_quarterly_revenue_report_no_merge (company_number,company_name,date,basepath,folder_name): 
    # get html data
    Stock_page = urllib.request.urlopen('http://cathaysec.moneydj.com/z/zc/zcd_%s_2.djhtm'%company_number)  #number only
    Stock_data = Stock_page.read().decode('big5','ignore')
    #print (Stock_data)

    # write files test
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(Stock_data)
    soup_formal = soup.prettify()
    #get formal data format
    Formal_data = open("%s/Formal_data.txt"%os.getcwd(), "wb")
    Formal_data.write(soup_formal.encode("utf-8"))
    Formal_data.close()

    #print(basepath)
    directory = basepath+"/%s/%s/"%(date,folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    resouce_data = open("Formal_data.txt","rb")
    parsing_data = open("%s/%s_%s.csv"%(directory,company_number,company_name),"w")
    stock_input_data = BeautifulSoup(resouce_data.read().decode("utf-8"))
    td_sum=""
    #skip top two table and last
    for table in stock_input_data.findAll("table")[2:-1]:
        #skip top four tr
        for tr in table.findAll("tr")[1:]:
            for td in tr.findAll("td"):
                td_result = td.text.strip() #remove empty space
                td_result = td_result.replace(',','')
                td_sum = td_sum + td_result + ","           
                #td_sum = td_sum.replace('\n',';')
                #print(td.text)
            print(td_sum)
            parsing_data.write(td_sum+"\n")
            td_sum="" #clear data   
    #wait = input("PRESS ENTER TO CONTINUE.") #wait for input key
    parsing_data.close()
    return 0
#=================================================================#
#=================================================================#
def merge_cvs_files(cvs_file_path):
    #===================================
    #Get files  and Main function
    #===================================
    for dirPath, dirNames, fileNames in os.walk(cvs_file_path):
        #for files in dirNames:
        #    print (os.path.join(dirPath, files))
        #for files in fileNames:
        #    print (os.path.join(dirPath, files))
                
        
        Write_back_file = xlwt.Workbook()
        sheet_list = []
        for sheets in fileNames:
            sheet_list.append(Write_back_file.add_sheet(sheets))
            #print(sheet_list)
        sheet_list_index = 0
        
        #read CSV FILE
        for FileName in fileNames:
            #if os.path.exists('%s/summary.xls'%(os.path.join(dirPath, dirNames))):
            #    print("exist~!")
            #else:
            CSV_Input = open(os.path.join(dirPath, FileName), 'r')
            X_axis = 0
            Y_axis = 0
            for csv_list_item in csv.reader(CSV_Input):
                #print(csv_list_item)
                #print(len(csv_list_item))
                X_axis = 0
                for X_axis_data in csv_list_item:
                    sheet_list[sheet_list_index].write(Y_axis, X_axis, X_axis_data)
                    X_axis = X_axis+1
                Y_axis = Y_axis +1
            Write_back_file.save('%s/summary.xls'%(os.path.join(dirPath, dirNames)))
            sheet_list_index = sheet_list_index + 1
    
    return 0
#=================================================================#
# Main function
#=================================================================#
import urllib.request 
print ("Hellow word")

#main program
import os
import sys
import xlwt3 as xlwt   #Excel file write
import csv             #CSV file read/write
#import ctypes          #windows message
import time
import datetime

#MessageBox = ctypes.windll.user32.MessageBoxW #python 3.x
#MessageBox(None, 'please wait till finish message', 'Merge', 0)

now = datetime.datetime.now()
date = "%s-%s-%s" % (now.year, now.month, now.day)
basepath = os.getcwd()+"/result"
#get compayn list
stock_names = open("stock_all.csv", "rb").read().decode('utf-8')
company_readline = stock_names.split("\n")

for company_number  in company_readline:
    '''
    #=================================================================#
    #  company_information
    #=================================================================#
    #print(company_number[:4])  #get company_number
    company_information(company_number[:4],company_number[5:],date,basepath,"basic_information")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    #  company_shareholding_distribution
    #=================================================================#
    #print(company_number[:4])  #get company_number
    company_shareholding_distribution(company_number[:4],company_number[5:],date,basepath,"shareholding_distribution")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    #  company_quarterly_revenue_report_no_merge
    #=================================================================#
    #print(company_number[:4])  #get company_number
    company_quarterly_revenue_report_no_merge(company_number[:4],company_number[5:],date,basepath,"quarter_revenue_no_merge")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    # company_quarterly_profit_report_merge
    #=================================================================#
    company_quarterly_profit_report_merge(company_number[:4],company_number[5:],date,basepath,"quarter_profit_merge")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    # company_quarterly_dividend_report_merge
    #=================================================================#
    company_quarterly_dividend_report_merge(company_number[:4],company_number[5:],date,basepath,"quarter_dividend_merge")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    '''
    #=================================================================#
    #  cash flow
    #=================================================================#
    company_cash_flow (company_number[:4],company_number[5:],date,basepath,"cash_flow")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    #  company_balance_sheet
    #=================================================================#
    company_balance_sheet (company_number[:4],company_number[5:],date,basepath,"balance_sheet")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    #  company_quarter_income_statement_sheet
    #=================================================================#
    company_quarter_income_statement_sheet(company_number[:4],company_number[5:],date,basepath,"quarter_income_sheet")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge
    #=================================================================#
    # company_quarter_financial_ratio_sheet
    #=================================================================#
    company_quarter_financial_ratio_sheet(company_number[:4],company_number[5:],date,basepath,"quarter_financial_ratio_sheet")
    time.sleep(3) #wait 2 seconds
    #remove temp files
    os.remove(os.getcwd()+"/Formal_data.txt") #company_quarterly_report_no_merge


#mrege cvs files
#merge_cvs_files(basepath)
