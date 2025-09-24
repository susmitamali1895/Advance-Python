#zip()
# zip = cobine iterables
a = [1,2,3]
b = ['a', 'b', 'c']
print(list(zip(a,b))) 

#enumerate = Index + item
for i, val in enumerate(['x','y']):
    print(i, val)