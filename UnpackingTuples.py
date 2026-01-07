#packing a tuple:
#fruits = ("apple", "banana", "cherry")
#(green , yellow, red) = fruits 
#print(green)
#print(yellow)
#print(red)

# Unpacking using Asterisk*
# Assign the rest of the values as a list called red:
fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")
(green, yellow, *red ) = fruits 
print(green)
print(yellow)
print(red)