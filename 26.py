import numpy as np

arr= np.array([[6.,7.,6.,9.,0.,5.,4.,0.,6.,8.,5.,2.,],
               [8.,5.,5.,7.,1.,8.,6.,7.,1.,8.,1.,0.,]])

x= np.hsplit(arr,3)

print("x= \n",x)

y=x.copy()

print("y= \n",y)

z=np.array([[0,1],[2,3]])

z=z.fill(1)

print("z= \n",z)