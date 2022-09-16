import numpy as np

test_list= [[5,6,8],[7,4,3], [8,10,12]]

mult_list= [10,20,30]

print("test_list= ", test_list)
print("LenTestList= ", len(test_list))

print("mult_list= ", mult_list)

res= [[] for idx in range(len(test_list))]
for i in range(len(test_list)):
    for j in range(len(mult_list)):
        res[i]+= [mult_list[i]*test_list[i][j]]

print("the list after multiply: \n", res)