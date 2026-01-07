#Change the original dict
#car = {
 #   "brand" :" ford",
  #  "model" : "Mustang", 
   # "year" : 1964
#}
##x = car.items()
#print(x) # before the change
#car["year"]= 2020
#print(x) #after the change 

#Check if key exist
#thisdict = {
#    "brand": "ford", 
#    "model" : "mustang",
#    "Year" : 1964
#}
#if "model" in thisdict:
#    print("Yes, 'model' is one of the key in the thisdict dictionary")

#Update Dictionary 
#thisdict.update({"Year":2020})
#print(thisdict)

#Adding Items
#thisdict["color"] = "red"
#print(thisdict)

#Removing Items 
#thisdict.pop("model")
#print(thisdict )

# The clear method empties the dictionary
#thisdict.clear()
#print(thisdict)

# The delete keyword can also delete the dictionary completely
#del thisdict
#print(thisdict)

#Copy a dictionary
#mydict = thisdict.copy()
#print(mydict) 

#Nested Dictionaries 
myfamily = {
    "child1": {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" :{
        "name" : "Tobies",
        "year" : 2007
    },
    "child3" :{
        "name" :"Linus",
        "year" : 2011
    }
}
print(myfamily)

# Print the name of child2
print(myfamily["child2"]["name"])