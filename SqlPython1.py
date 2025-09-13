import mysql.connector
#connect to mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Susmita@18",
    database = "sqlpython"
)
print("Connected Successfully")
#create a curser 
mycursor = mydb.cursor()
# create a new table 
mycursor.execute ("""
    CREATE TABLE IF NOT EXISTS students(
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(255)
                  age INT
                  )
                  """)
print("Table created successfully")

