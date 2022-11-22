#EXERCISE 1 - Element-wise addition of 2 numpy arrays

#Given are 2 similar dimensional numpy arrays, how to get a numpy array output in
#which every element is an element-wise sum of the 2 numpy arrays?

import numpy as np

a= np.array([[1,2,3,4],
             [5,6,7,8]])
b= np.array([[8,7,6,5],
             [4,3,2,1]])

c=a+b
print("Sum= \n", c)