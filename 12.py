import numpy as np

arr= np.array([[1,5,6],
               [4,7,2],
               [3,1,9]])
print("arrMAX= ", arr.max())
print("arrRowMAX= ", arr.max(axis=1))
print("arrColumnMIN= ", arr.min(axis=0))
print("arrSum= ", arr.sum())
print("arrRowSum= \n", arr.cumsum(axis=1))
print("arrColumnSum= \n", arr.cumsum(axis=0))