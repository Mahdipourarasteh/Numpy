import numpy as np

c= np.array([[0,1,2,3],
             [10,11,12,13],
             [20,21,22,23],
             [30,31,32,33],
             [40,41,42,43]])

for row in c:
    print(row)

for element in c.flat:
    print(element)