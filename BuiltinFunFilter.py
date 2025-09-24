#filter()
#Filters item from an iterable based on a function that returns True or False
nums = [1,2,3,4,5]
evens = filter (lambda x: x%2==0, nums)
print(list(evens))
