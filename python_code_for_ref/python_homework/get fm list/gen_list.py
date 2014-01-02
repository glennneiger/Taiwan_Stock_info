
import os
import time
import datetime
import random


Output_list_file = open("Sky_FM.list", "w")
Input_list_file = open("orignal_list.data","r").read().split(",")
#print(Input_list_file[4].find("http"))
row_num = len(Input_list_file)
#list_number = 0
#URL_list = [None] * 300
URL_list = [] 
Name_list = [] 
#print(row_num)
for loop_num in range(len(Input_list_file)):
    #print(loop_num)
    if(Input_list_file[loop_num].find("name")>0):
        Name_list = Input_list_file[loop_num].replace("\"name\":\"","")
        Name_list = Name_list.replace("\"","")     
        #print(Name_list[list_number])
        print("#SKY FM:%s \n"%Name_list)
        Output_list_file.write("#SKY FM:%s \n"%Name_list)
        
    if(Input_list_file[loop_num].find("http")>0):
        #print(Input_list_file[loop_num])
        URL_list = Input_list_file[loop_num].replace("\"playlist\":\"","") 
        URL_list = URL_list.replace("\"}","")     
        URL_list = URL_list.replace("]","")                #last one
        #print(URL_list[list_number])
        print("mplayer –o oss –cache 256 –playlist %s < /dev/null \n&"%URL_list)
        Output_list_file.write("mplayer –o oss –cache 256 –playlist %s < /dev/null & \n"%URL_list)


#Input_list_file.close()
Output_list_file.close()

#SKY FM: xxxx
#mplayer –o oss –cache 256 –playlist TheURLOfxxxx < /dev/null &

