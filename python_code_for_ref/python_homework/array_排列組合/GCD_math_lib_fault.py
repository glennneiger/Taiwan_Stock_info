'''
Created on 2013/4/30

@author: JKZhong
'''
from numpy  import *



def prim_list(Input_number):
    prime_index = 0
    prime_num = array( [2] , dtype=int32)
    #print(prime_num)
    #print(prime_num.size)
    #print(prime_num[0])
    
    if(Input_number<2):
        print("There is no prime number\n")
    for loop_number in range(2,Input_number+1): #start at three 
        #print ("loop_number:%d"%loop_number)
        No_match_old = 1
        for prime_len_loop in range(prime_num.size):
            #print ("prime_len_loop:%d"%prime_len_loop)
            if (loop_number%prime_num[prime_len_loop] == 0):
                #print("No.%d Match case: %d"%(loop_number,prime_num[prime_len_loop]))
                No_match_old = 0
                break
        if(No_match_old):   #no match old prime number
            prime_num.resize(prime_num.size + 1)        #increase array size
            prime_num[prime_num.size - 1] = loop_number #index from 0, so -1
            #print("Save prime, number is %d"%loop_number)
    return(prime_num)

#================================================================#
def factor_list(Input_number):
    prim_num_array = prim_list(Input_number)
    factor = []
    not_find_end = 1
    prime_index_increase = 0
    factor_index_increase = 0 
    while not_find_end:
        if(Input_number%prim_num_array[prime_index_increase] ==0):
            #print(prim_num_array[prime_index_increase])
            Input_number = Input_number/prim_num_array[prime_index_increase]
            #print(Input_number)
            #factor[factor_index_increase] = prim_num_array[prime_index_increase]
            factor.append(prim_num_array[prime_index_increase])
            factor_index_increase = factor_index_increase + 1 
        elif (Input_number!= 1 ): 
            prime_index_increase = prime_index_increase +1
            #break
        else: #last one
            #factor[factor_index_increase] = prim_num_array[prime_index_increase]
            not_find_end = 0
    #print("result:%s"%factor)
    return(factor)


#=============  main program  ============================#
'''
use list and set to filter same item. 
'''
Data_first = (set(factor_list(50)))  
Data_second = (set(factor_list(24)))
#Find greatest common multiple
GCM_MCD_list = list(Data_first.intersection(Data_second)) #Common element
sorted(GCM_MCD_list) #list can sort
GCM = GCM_MCD_list[len(GCM_MCD_list)-1]
MCD = GCM_MCD_list[0]
print(Data_first)
print(Data_second)
print(GCM_MCD_list)
print(GCM)
print(MCD)

#Find greatest common divisor 

#Data_first.sort(reverse=False)




'''
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]

sorted(strs, reverse=True)   # ['zz', 'aa', 'CC', 'BB']
http://swaywang.blogspot.tw/2012/05/pythonpythonpython-sorting.html
'''