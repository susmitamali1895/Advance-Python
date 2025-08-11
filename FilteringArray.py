#create an array from the elements on index0 and 2
import numpy as np
arr = np.array([41,42,43,44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
#the only numbers are printed whose value is True
# both arrays are compaired with each other and only printed the True 