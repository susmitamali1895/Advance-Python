#what if a value can not be Converted?
#If a type is given in which elements cant be casted then Numpy will raise a ValueError
#ValueError-In Python ValueError is raised when the typr of passed argument to a function is unexpected/ incorrect
# ex. A non integer string like 'a' can not be converted to integer(will raise an error) 
import numpy as np
arr = np.array(['a','2','3'], dtype='i')
