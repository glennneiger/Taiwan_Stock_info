import os 
import time
import xlwt3 as xlwt   #Excel file write
import csv             #CSV file read/write
import ctypes          #windows message
from datetime import datetime

#current_date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
current_date = time.strftime("%Y_%m_%d", time.gmtime())
#wait for write finish
MessageBox = ctypes.windll.user32.MessageBoxW #python 3.x

#===================================
#Get files  and Main function
#===================================
for dirPath, dirNames, fileNames in os.walk("./Result_files"):
    print (dirPath)
    for f in fileNames:
        print (os.path.join(dirPath, f))
print(dirPath)        
print(len(fileNames))

#define_excel_sheet
Write_back_file = xlwt.Workbook()
sheet_list = []
for sheets in fileNames:
     sheet_list.append(Write_back_file.add_sheet(sheets))
#print(sheet_list)

sheet_list_index = 0

MessageBox(None, 'Excel merge... please wait till finish message', 'Merge', 0)
#read CSV FILE
for FileName in fileNames:
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
    
    Write_back_file.save('Lai_thesis_data_%s.xls'%current_date)
    sheet_list_index = sheet_list_index + 1
    

MessageBox(None, 'Excel merge finish', 'Window title', 0)





'''       
for Files_list in fileNames:
    #print(Files_list.find("csv"))
    if(Files_list.find("csv") > 0):
        csv_list = []
        print(Files_list)
        Processing_CVS_FILE_TO_EXCELL(Files_list)
'''        
        
        
        

'''
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                     num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
'''