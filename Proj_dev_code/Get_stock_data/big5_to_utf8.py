
file_big5 = open("stock_all.csv","rb").read().decode("big5","ignore")
file_utf8 = open("stock_all_utf.csv","wb")

file_utf8.write(file_big5.encode("utf-8","ignore"))
file_utf8.close()


'''
import os
folder_list = os.listdir(basepath)
lasted_data = basepath+"/%s"%folder_list[-1]
for folders in os.listdir(lasted_data):
    for files in os.listdir(lasted_data+"/%s"%folders):
'''
