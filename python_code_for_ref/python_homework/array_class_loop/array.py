class test_struct:
    x = 0
    y = 0

temp_data = [[None for x in range(6)] for y in range(6)]

for loop_x in range(6):
    for loop_y in range(6):
        temp_data[loop_y][loop_x] = test_struct()
print(temp_data)
