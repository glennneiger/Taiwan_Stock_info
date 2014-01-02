'''
Created on 2013/4/30

@author: JKZhong
'''

def Get_Div_list(Input_data):
    Div_list = []
    for i in range (1,Input_data+1):
        if Input_data%i == 0:
            Div_list.append(i)
    return(Div_list)
    
#==========   main ============================//
Data_a = 18
Data_b = 24

First_list_element = Get_Div_list(Data_a)
Second_list_element = Get_Div_list(Data_b)
The_same_list = list(set(First_list_element).intersection(set(Second_list_element)))
#Find greatest common divisor 
GCD = The_same_list[len(The_same_list) - 1]  
print("GCD:%d"%GCD)

LCM = abs(Data_a*Data_b)/GCD
print("LCM:%d"%LCM)


