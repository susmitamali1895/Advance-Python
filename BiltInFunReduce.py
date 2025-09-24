#reduce 
#reduces an iterable to a single value using a bonary fuction(Needs functools)
from functools import reduce
nums =[1,2,3,4]
product= reduce(lambda x,y:x*y, nums)
print(product)