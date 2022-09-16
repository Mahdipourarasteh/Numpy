import numpy as np

a= np.array([[1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]])

print("a= \n", a)

print("shape=",a.shape)

print("ravel=",np.ravel(a))

print(a.reshape(6,2))
