#!/usr/bin/env python
# -*- coding: utf-8 -*-
#這裡將日盛網頁資料，分成index, data兩個檔案切出需要的文字後，再合併
#最後再重新整理資料，因為網頁的資料表格，有橫、直之分，所以資料有些分散
#要注意網頁的編碼、<p>標籤會多一次的取值
#import htmldom
from htmldom import htmldom


def html_parser(path_time,path_stock,path_file):
    #print(path_time)
    #print(path_file)
    #print(path_file)
    print("web_data\%s\%s\%s.djhtm" %(path_time,path_stock,path_file))
    dom_temp = open("web_data\%s\%s\%s.djhtm" %(path_time,path_stock,path_file),"r")
    dom = dom_temp.read()
    #print( dom )
    dom_htmldom = htmldom.HtmlDom().createDom(dom)
    error_page = dom.find("無此股票資料")#error
    if(error_page==-1):
        print("ok")
    else:
        print("error page")
        return(1)
    #print( dom_htmldom )
    index_element = dom_htmldom.find("td .t4t1") #index file use it
    index_useless = {"董事長","總經理","發言人","營收比重","公司電話","網址","公司地址","說明"}
    index_match = 0
    #index fillter data
    index_file = open("web_data\%s\%s\index_file" %(path_time,path_stock),"w")
    for x in index_element:
        for y in index_useless:
            if(x.text() == y):
                index_match =1
        if(index_match == 0):
            index_file.write(x.text())
            index_file.write("\n")
        index_match =0
    index_file.close()
    #data###################################################################################33            
    data_element = dom_htmldom.find("td .t3n1")
    data_element_usless = dom_htmldom.find("td .t3n1 .t3n1") #cause <p> will one more record
    #print(data_element.text())
    data_unit =1
    
    #data fillter data        
    data_file_temp = open("web_data\%s\%s\data_file_temp" %(path_time,path_stock),"w")
    for x in data_element:
        #print(x.text(0))
        for y in data_element_usless:
            if(x.text()==y.text()):
                data_unit = 0
        if(data_unit == 1):  #correct data  #cause <p> will one more record
            data_file_temp.write(x.text())
            data_file_temp.write("\n")
        data_unit =1  #get next data
    data_file_temp.close()
    #cut space in file
    data_file_temp = open("web_data\%s\%s\data_file_temp" %(path_time,path_stock),"r")
    data_file = open("web_data\%s\%s\data_file" %(path_time,path_stock),"w")
    for x in data_file_temp:
        if(x!="\n"):
            data_file.write(x)
    
    data_file_temp.close()
    data_file.close()        
    
    #combin index and data
    index_file = open("web_data\%s\%s\index_file" %(path_time,path_stock),"r").read().split("\n")
    data_file = open("web_data\%s\%s\data_file" %(path_time,path_stock),"r").read().split("\n")
    finance_basic_file_temp = open("web_data\%s\%s\\finance_basic_file_temp" %(path_time,path_stock),"w")
    str_data =""
    #print (index_file[0])
    for loop_num in range(58):
        #print(loop_num)
        finance_basic_file_temp.write(index_file[loop_num]+" "+data_file[loop_num]+"\n")
            
    for loop_num in range(58,64):
        #print(loop_num)
        for x in range(6):
            str_data = (str_data+" "+data_file[loop_num+x])
        finance_basic_file_temp.write(index_file[loop_num]+str_data+"\n")
        str_data =""
    
    #year infor
    enable =0
    str_data =""
    year_element = dom_htmldom.find("td .t4t")
    for x in year_element:
        if(x.text() == "年度"):
            enable =1
            str_data = x.text()
        if(enable & int(x.text()!="年度")):
            str_data = (str_data+" "+x.text())
    #print(str_data)
    finance_basic_file_temp.write(str_data+"\n")        
    finance_basic_file_temp.close()
    
    
    #############################################################################
    #重新整理資料
    ####################
    #稅額扣抵率
    #投資報酬率
    #財務比例
    #投資風險
    #基本資料
    #獲利能力
    #前一年度配股
    #財務預測#
    ########################################################################
    finance_basic_file_temp = open("web_data\%s\%s\\finance_basic_file_temp" %(path_time,path_stock),"r")
    finance_basic_file = open("web_data\%s\%s\\finance_basic_file.txt" %(path_time,path_stock),"w")
    
    str_input =finance_basic_file_temp.readlines() 
    #print(finance_basic_file_temp.readlines()[13])
    str_data=""
    for x in range(18):
    	#print(str_input[x])
        str_data =str_data+str_input[x]
    #print(str_data)
    #稅額扣抵率
    str_0 = "稅額扣抵率\n"+str_input[22]+str_input[26]+str_input[29]+str_input[32]+str_input[35]
    #print(str_0)
    #投資報酬率
    str_1 = "投資報酬率\n"+str_input[19]+str_input[23]+str_input[27]+str_input[30]+str_input[33]
    #財務比例
    str_2 = "財務比例\n"+str_input[20]+str_input[24]+str_input[28]+str_input[31]+str_input[34]+str_input[36]
    #投資風險
    str_3 = "投資風險\n"+str_input[21]+str_input[25]
    #基本資料
    str_4 = "基本資料\n"+str_input[37]+str_input[41]+str_input[45]+str_input[49]
    #獲利能力
    str_5 = "獲利能力\n"+str_input[38]+str_input[42]+str_input[46]+str_input[50]
    #前一年度配股
    str_6 = "前一年度配股\n"+str_input[39]+str_input[43]+str_input[47]+str_input[51]+str_input[54]+str_input[56]+str_input[57]
    #財務預測#
    str_7 = "財務預測\n"+str_input[40]+str_input[44]+str_input[48]+str_input[52]+str_input[55]
    #年度資料
    str_8 = "年度資料\n"+str_input[64]+str_input[58]+str_input[59]+str_input[60]+str_input[61]+str_input[62]+str_input[63]
    
    str_data =str_data+str_0+str_1+str_2+str_3+str_4+str_5+str_6+str_7+str_8
    #print(str_data)
    finance_basic_file.write(str_data)
    finance_basic_file.close()
    return(0) #finish program


#test thins function

#a="2012-11-4"
#b="1108幸福"
#c="基本資料1108"
#b="1101台泥"
#c="基本資料1101"
#html_parser(a,b,c)













