# to overwrite the exixting content to file, use w parameter
# open the file demofile.txt and overwrite the content
with open("demofile.txt", "w") as f:
    f.write("Woops ! I have deleted the content!")
#open and red the file after the overwriting 
with open("demofile.txt") as f:
    print(f.read())