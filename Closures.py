#inner function remember the environment in which they were created 
def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
    
double = make_multiplier(2)
print(double(5))

