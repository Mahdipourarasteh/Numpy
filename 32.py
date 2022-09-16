import numpy as np

in_array= [.5,1.5,2.5,3.5,4.5,10.1]
print("Input array=\n", in_array)

round_of_values= np.round_(in_array)
print("\nRounded Values_\n", round_of_values)
print("---------------------------------------")
#############################################################
in_array= [.53,1.54,.71]
print("Input array=\n", in_array)

round_of_values= np.round_(in_array)
print("\nRounded Values_\n", round_of_values)
print("---------------------------------------")
############################################################
in_array= [.5538,1.33354,.71445]
print("Input array=\n", in_array)

round_of_values= np.round_(in_array, decimals=3)
print("\nRounded Values_\n", round_of_values)