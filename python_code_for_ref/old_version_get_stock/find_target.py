import os

def find_target(path_time,path_stock,path_file):
    #print(path_time)
    #print(path_file)
    #print(path_file)
    print("web_data\%s\%s\%s" %(path_time,path_stock,path_file))
    basic_data = open("web_data\%s\%s\%s" %(path_time,path_stock,path_file),"r")

    path ='web_data\%s\\result' %(path_time)
    if not os.path.exists(path):
        os.mkdir(path)    
    else:
        pass

    #執行挑選公式
    constrain_1(path_time,path_stock,basic_data)#預期殖利率
    
    basic_data.close()
    return(0)
    
def constrain_1 (path_time,path_stock,orignal_data): #預期殖利率, 貝他值, 營業利益率
    stock_yield=0
    stock_bate_value=0
    stock_Operating_Margin=0
    file_data = orignal_data.readlines()
    #選資料
    for x in file_data:
        line_data = x.split(" ")
        if(line_data[0] == "殖利率"):
            #print(type(line_data[1][:4]))  本來就是字串，無法判斷錯誤
            stock_yield=float(line_data[1][:4])
            #print(stock_yield)
        if(line_data[0] == "貝他值"):
            stock_bate_value=float(line_data[1])
            print(stock_bate_value)
        if(line_data[0] == "營業利益率"):
            stock_Operating_Margin=float(line_data[1][:4])
            print(stock_Operating_Margin)
    #判斷公式
    if((stock_yield > 8.0) & (stock_bate_value < 1.0) & (stock_Operating_Margin > 10.0)):
        result_file = open("web_data\%s\\result\%s" %(path_time,path_stock),"w")
        result_file.write(" ")
        result_file.close()
        
    return(0)




#a="2012-11-4"
#b="1108幸福"
#c="基本資料1108"
#b="1101台泥"
#c="finance_basic_file.txt"
#find_target(a,b,c)
    
