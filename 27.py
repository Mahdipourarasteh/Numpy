import numpy as np

a= np.linspace(2.0,3.0,num=12)
print(a)
print("-----------------------")

s=np.linspace(2.0,3.0,num=12,endpoint=False)
print(s)
print("-----------------------")

w=np.logspace(2.0,3.0,num=4)             #logarithm of 4 numbers between 2 and 3
print(w)
print("-----------------------")

q=np.logspace(2.0,10.0,num=4,endpoint=False)
print(q)