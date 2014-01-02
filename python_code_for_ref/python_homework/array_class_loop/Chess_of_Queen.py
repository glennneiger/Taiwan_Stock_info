from numpy  import *
Queen = 4

row_fill = array([0],dtype=int32)
row_fill.resize(row_fill.size + (Queen-1))
print(row_fill)
'''
row_fill[0]=1
row_fill[1]=1
row_fill[2]=1
row_fill[3]=1
print(row_fill)
'''

#define data struct
class Point_Data:
    set_point   = 0
    right_limit = 0
    left_limit  = 0

#count data array
array_of_matrix = [[None for x in range(Queen)] for y in range(Queen)]
#drow diagram array
array_of_matrix_draw = array([], dtype=int32)
array_of_matrix_draw.resize(Queen*Queen)    #tatol size
array_of_matrix_draw.shape = (Queen,Queen)  #2-D

print(array_of_matrix)
#build up struct
for loop_x in range (Queen):     # x direction
    for loop_y in range (Queen): # y direction
        array_of_matrix[loop_x][loop_y] = Point_Data()
#print(array_of_matrix[0][1].right_limit)

for X_Dir in range (Queen):
    for Y_Dir in range (Queen):
        #select point
        if((array_of_matrix[X_Dir][Y_Dir].set_point | array_of_matrix[X_Dir][Y_Dir].right_limit | array_of_matrix[X_Dir][Y_Dir].left_limit) == 0):
            array_of_matrix[X_Dir][Y_Dir].set_point = 1
            array_of_matrix_draw[X_Dir][Y_Dir] = 1
        #add limitation
            
        
#Check result 
for check_row_loop in range(Queen):
    if row_fill[check_row_loop] == 1:
        if check_row_loop != Queen-1:
            #print(check_row_loop)
            continue
        else:
            print("finish serach")
    else :
        print("not finish")
        break




'''
array_of_matrix = array([], dtype=int32)
array_of_matrix.resize(Queen*Queen)    #tatol size
array_of_matrix.shape = (Queen,Queen)  #2-D

counter=0
for loop_x in range (4):     # x direction
    for loop_y in range (4): # y direction
        array_of_matrix[loop_y][loop_x] = counter
        counter = counter +1
print (array_of_matrix)
print (array_of_matrix[1])
print (array_of_matrix[2-1][1-1])
'''
