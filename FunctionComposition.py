#combine simple function to build complex ones
def double(x): return x*2
def increment(x): return x+1

def compose(f, g):
    return lambda x:f(g(x))
new_func= compose(double, increment)
print(new_func(3))  #(3+1)*2=8