#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 註解
#print ('Hello word')
#import StringIO

import os
import time
import datetime
import random
import urllib.request
import html_parser
import find_target

def line_count(filename):
    '''Count file's lines neglect '\n' '''
    count=0
    #print filename
    for line in open(filename):
        if(line!='\n'):count+=1
    return count
#================================= main program =================================================#
#build up folder to save data
now = datetime.datetime.now()
date ="%s-%s-%s" % (now.year, now.month, now.day)
#web_data folder
#path = 'c:\Users\JKZhong\Desktop\get_stock\web_data'
path ='web_data'
if not os.path.exists(path):
    os.mkdir(path)    
else:
    pass

#data folder
#path ="c:\Users\JKZhong\Desktop\get_stock\web_data\%s" % date
path ='web_data\%s' %(date)
if not os.path.exists(path):
    os.mkdir(path)    
else:
    pass


#================================= get data from web =================================================#
file_line_num = line_count("stock_list.txt")
stock_list = open("stock_list.txt" , "r").read().split("\n") #每行的資料都變成陣列
#print (stock_list)

#for stock_list_loop in range(2):
for stock_list_loop in range(file_line_num):
    stock_number = stock_list[stock_list_loop].split("\t")[0]  #取出每行，再切出股號
    print (stock_number)

    #=============================================================#
    #data folder
    path ='web_data\%s\%s%s' %(date,stock_number,stock_list[stock_list_loop].split("\t")[1])
    if not os.path.exists(path):
        os.mkdir(path)    
    else:
        pass


    #get web data
    content = urllib.request.build_opener()
    content.addheaders = [('User-agent', 'Mozilla/5.0')]
    
    #zca 基本資料 日盛
    url = 'http://jsjustweb.jihsun.com.tw/z/zc/zca/zca_%d.djhtm'% int(stock_number)  #網頁股號的字串處理
    print (url)
    
    content = urllib.request.urlopen(url)
    content = content.read()
    content_str = content.decode('big5','ignore')

    zca_file = open(path+"\基本資料%d.djhtm" % int(stock_number) , "wb")
    #zca_file.write(content_str.encode('utf-8', 'ignore'))
    zca_file.write(content_str.encode('big5', 'ignore'))
    zca_file.close()


    #zch 月營收
    #url = 'http://jsjustweb.jihsun.com.tw/z/zc/zch/zch_%d.djhtm'% int(stock_number)  #網頁股號的字串處理
    #content = urllib.request.urlopen(url)
    #content = content.read()
    #content_str = content.decode('big5','ignore')
    #zca_file = open(path+"\月營收%d.djhtm" % int(stock_number) , "wb")
    #zca_file.write(content_str.encode('big5', 'ignore'))
    #zca_file.close()

    time.sleep(random.randint(1, 5) )
	
    path_stock = (stock_number+stock_list[stock_list_loop].split("\t")[1])
    path_file = "基本資料"+stock_number
    #處理網頁資料
    print("call html_parser")
    error = html_parser.html_parser(date,path_stock,path_file)

    #找結果
    if(error == 0):#erro 網頁不存在
        try:
            find_target.find_target(date,path_stock,"finance_basic_file.txt")
        except:
            print("target may be error")


    

