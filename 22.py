import numpy as np

a=np.array([[1,2],
            [3,4]])
print("a= \n",a)

b=np.array([[5,6],
            [7,8]])
print("b= \n",b)

print("vstack= \n", np.vstack((a,b)))
print("hstack= \n", np.hstack((a,b)))