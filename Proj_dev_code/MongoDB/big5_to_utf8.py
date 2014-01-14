import os
basepath = os.getcwd()+"/result"
folder_list = os.listdir(basepath)
lasted_data = basepath+"/%s"%folder_list[-1]
for folders in os.listdir(lasted_data):
    for files in os.listdir(lasted_data+"/%s"%folders):
        file_path = lasted_data+"/%s"%folders+"/%s"%files  
        print(file_path)
        input("wait_key")
        file_big5 = open(file_path,"r").read()
        temp_file = file_big5
        print(file_big5)        
        input("wait_key")
        
        file_utf8 = open(file_path,"wb")
        file_utf8.write(temp_file.encode("utf-8","ignore"))
        file_utf8.close()
        input("wait_key")
