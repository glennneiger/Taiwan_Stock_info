import os
basepath = os.getcwd()+"/result"
#for dirpath, folders, files in os.walk(basepath):
folder_list = os.listdir(basepath)
#print(folder_list[-1])  #get latesed data

lasted_data = basepath+"/%s"%folder_list[-1]
#print(lasted_data)

#for dirpath, folders, files in os.walk(lasted_data)
#print(os.listdir(lasted_data))
for folders in os.listdir(lasted_data):
    #print(folders)
    #print(os.listdir(lasted_data+"/%s"%folders))
    for files in os.listdir(lasted_data+"/%s"%folders):
        #print(files)
        file_path = lasted_data+"/%s"%folders+"/%s"%files
        #print(os.path.getsize(lasted_data+"/%s"%folders+"/%s"%files))
        #input(file_path)
        #input("wait")
        if os.path.getsize(file_path) <  100:
            print(files)
            os.remove(file_path)
        

