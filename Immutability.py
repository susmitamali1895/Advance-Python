# mutable 
lst = [1,2,3]
lst.append(4)
print(lst) #modifies list


#Immutable 
tup=(1,2,3)
new_tup = tup + (4,)
#print(new_tup) #returns new tuple