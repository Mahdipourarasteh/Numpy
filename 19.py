from gettext import npgettext


import numpy as np

def f(x,y):
    return 10*x+y

b= np.fromfunction(f,(5,4),dtype=int)
print("b= \n", b)

print("b[2,3]= \n", b[2,3])

print("b[0:5,1]= \n", b[0:5,1])
print("b[ : ,1]= \n", b[ : ,1])

print("b[1:3, : ]= \n", b[1:3, : ])