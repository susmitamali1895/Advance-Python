import mysql.connector
# connect to mysql
mydb = mysql.connector.connect(
    host ="localhost",                   #or your server host
    user= "root",                        #your Mysql username
    password= "Susmita@18",              #your mysql password
    database = "pythonmysqlconnect"      #optional: the db to use
)
print("Connect Successful")

#create a cursor
mycursor = mydb.cursor()
#create a new table
#mycursor.execute("""
                 #CREATE TABLE IF NOT EXISTS students(
                 #id INT AUTO_INCREMENT PRIMARY KEY,
                 #name VARCHAR(255),
                 #age INT
                 #)
                 #""")
# print("Table created successfully")
#sql = "INSERT INTO students(name, age) VALUES (%s, %s)"
#val = ("John", 21)
#mycursor.execute(sql,val)
#mydb.commit()
#print(mycursor.rowcount, "record inserted")
mycursor.execute("SELECT *FROM students")
result = mycursor.fetchall()
for row in result:
    print(row) 
