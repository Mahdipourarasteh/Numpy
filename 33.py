import numpy as np
import numpy.ma as ma

a1= np.array([1,2,3])
a2= np.array([4,5,6])

a= ma.concatenate([a1,a2])
print(a)

b= ma.concatenate([[a1],[a2]])
print(b)