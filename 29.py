import numpy as np

a= np.arange(12).reshape(3,4)
print(a)
print("------------------")

i=np.array([[0,1],
            [1,2]])
print(a[i])
print("------------------")

j=np.array([[2,1],
            [3,3]])

print("index is: ", a[i,j])
print("-------------------")

print(a[i,2])