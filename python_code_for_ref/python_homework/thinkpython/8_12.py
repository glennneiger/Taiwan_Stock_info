lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(upper_case.rindex("J"))

def rotate (Data_in, rotate):
    Data_out=[]
    for word in Data_in:
        index=0
        if word.islower():
            index_num = lower_case.rindex(word)
            index = index_num + rotate
            if index >25 :
                index = 26 - index
            Data_out.append(lower_case[index])
            print(Data_out)
        elif word.islower():
            index_num = upper_case.rindex(word)
            index = index_num + rotate
            if index >25 :
                index = 26 - index
            Data_out.append(upper_case[index])  
            print(Data_out)            
        else:
            return(-1)
    return(Data_out)

test_string = "cheer"
print ("".join(list(rotate(test_string,7))))
