#functions that take other functions as argument or return them
def apply_twice(func, x):
    return func(func(x))
print(apply_twice(lambda x: x +1 ,3))