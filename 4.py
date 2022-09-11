import numpy as np

b= np.array([2,3,5,4])
print(b)
print(type(b))

c= np.array([(1.5,2,3), (4,5,6)])
print("c is: ", c)
print('--------------')

print(np.where(c>5, c,0))
print('-----------------')
print()

d= np.arange(24).reshape(2,3,4)
print("d is: ",d)
print()

s= np.arange(10000)
print("s is: ",s ,"index98 is ",s[98])
print()

print(np.arange(10000).reshape(5,20,100))