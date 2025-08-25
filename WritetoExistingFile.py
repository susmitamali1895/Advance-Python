# write to an existing file
with open("demofile.txt", "a") as f: #open the file
    f.write("Now the file has more content!") #write content in it

with open("demofile.txt", ) as f: #again open 
    print(f.read()) # read