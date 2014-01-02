'''
import sys
Year = int(sys.argv[1])
Month = int(sys.argv[2])
Day = int(sys.argv[3])
'''
Year = 1984
Month = 4
Day = 29
print("Year:%d, Month:%d, Day:%d"%(Year,Month,Day))

#year pluse a day 
if Year%400 == 0:
    print("plust a day; 400year")
    plus_day = 1
elif Year%100 == 0:
    plus_day = 0
elif Year%4 == 0:
    print("plust a day; 4year")
    plus_day = 1
else:
    plus_day = 0

#month day
Month_day = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
    }

Sum_day = Month_day[Month] + Day +plus_day

print("The day of this year: %d \n"%Sum_day)
print("reference data : http://zh.wikipedia.org/wiki/%E5%85%AC%E5%8E%86")


'''
print ("Multiline comment block" )
#case switch in python
Month_day=0
Month_day = {
    1:lambda x:31,
    2:lambda x:28,
    3:lambda x:31,
    4:lambda x:30
    5:lambda x:31
    6:lambda x:30
    7:lambda x:31
}[Month](Month_day)

print(Month_day)
'''
