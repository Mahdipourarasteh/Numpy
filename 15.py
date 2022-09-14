import numpy as np

a= np.array= ([[1,4,2],
               [3,4,6],
               [0,-1,5]])
print("sorted array: \n", np.sort(a, axis= None))

print("Row sorted array: \n", np.sort(a, axis= 1))

print("Coulmn merged sort: \n", np.sort(a, axis=0, kind='mergesort'))



dtypes= [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

values= [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
         ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arr= np.array(values, dtype = dtypes)                  ######?????????????

print("array sorted by names: \n", np.sort(arr, order='name'))
print("array sorted by graduation year and then cgpa: \n", np.sort(arr, order=['grad_year', 'cgpa']))
