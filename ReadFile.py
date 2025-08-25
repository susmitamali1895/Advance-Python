#f = open("demofile.txt")
#print(f.read())
# if file is not on same location, open a file on different location
# f = open("D:\\myfiles\welcome.txt")
#print(f.read())

#using with statement, You can also use the with statement when opening a file
with open("demofile.txt") as f:
    print(f.read())