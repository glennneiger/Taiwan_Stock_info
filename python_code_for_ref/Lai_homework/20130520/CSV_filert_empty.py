import os
import csv

def Get_File_len (Inpu_Data):
    index=0
    while Inpu_Data.readline():
        index = index + 1
    return (index)

def CSV_filert_empty(dirPath,FileName):
    #CSV_file = open('./Source_file/23電子.csv', 'r')
    #CSV_Clean_file = open('./Source_file/23電子_clean.csv', 'w')
    CSV_file = open(os.path.join(dirPath, FileName), 'r')
    FileName_clean = FileName+"_clean"
    CSV_Clean_file = open(os.path.join(dirPath, FileName_clean), 'w')
    #Read_line = csv.reader(CSV_file)
    Clean_data = []
    index=0
    file_length = Get_File_len(CSV_file)
    CSV_file.seek(0)
    print(file_length)
    
    for loop in range(file_length):
        Read_line = CSV_file.readline().split(",")
        #print(Read_line)    
        not_empty = 0
        for element in Read_line:
            if element == '' :
                print("empty")
                not_empty = 1
                break
            #else:
            #    continue
        
        print(Read_line)
        #input("Press Enter to continue...")
        if not_empty == 0:
            for index in range(len(Read_line)):
                if(index<len(Read_line)-1):
                    CSV_Clean_file.write("%s,"%Read_line[index])
                else:
                    CSV_Clean_file.write("%s"%Read_line[index])
            #print(Clean_data)
    CSV_file.close()        
    CSV_Clean_file.close()
    
    #replace file
    os.rename(os.path.join(dirPath, FileName), os.path.join(dirPath, FileName+"org"))
    os.rename(os.path.join(dirPath, FileName_clean), os.path.join(dirPath, FileName))
    #os.remove(os.path.join(dirPath, FileName_clean))
    