import numpy as np

a= np.array([1,2,5,3])

print("a+1= ",a+1)
print("a-3= ",a-3)
print("a*10= ",a*10)
print("a**2= ",a**2)

a *= 2
print("2a= ",a)

b= np.array([[1,2,3], [3,4,5], [9,6,0]])
print("b= ", b)
print("b Transpose= ", b.T)
