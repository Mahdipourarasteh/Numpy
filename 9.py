import numpy as np

a= np.array([[1,2,4], [5,8,7]], dtype ='float')
print("a= ", a)

b= np.array((1,3,2))
print("b= ", b)

c= np.zeros((3,4))
print("c= ", c)

d= np.full((3,3), 6, dtype= 'complex')
print("d= ", d)

e= np.random.random((4,4))
print("e= ", e)

f= np.arange(0,30,5)
print("f= ", f)

g= np.linspace(0,5,10)
print("g= ", g)

arr= np.array([[1,2,3,4],
                [5,2,4,2],
                [1,2,0,1]])
newarr= arr.reshape(2,2,3)
print("arr= ", arr)
print("newarr= ", newarr)

arr1= np.array([[1,2,3], [4,5,6], [8,9,10]])
flarr= arr.flatten()
print("flarr= ", flarr)

