import numpy as np

in_array1= np.array([1,2,3])
print("input1= \n", in_array1)

in_array2= np.array([4,5,6])
print("input2= \n", in_array2)

out_array= np.column_stack([in_array1, in_array2])
print("output= \n", out_array)