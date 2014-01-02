#down array library from :  http://www.numpy.org/
from numpy  import *
Input_number = 400


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
            print("No.%d Match case: %d"%(loop_number,prime_num[prime_len_loop]))
            No_match_old = 0
            break
    if(No_match_old):   #no match old prime number
        prime_num.resize(prime_num.size + 1)        #increase array size
        prime_num[prime_num.size - 1] = loop_number #index from 0, so -1
        print("Save prime, number is %d"%loop_number)
            
print(prime_num)




