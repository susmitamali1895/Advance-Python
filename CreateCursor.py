# create a cursor
mycursor = mydb.cursor()
#create a new table
mycursor.execyte("""
                 CREATE TABLE IF NOT EXISTS students(
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(255),
                 age INT
                 )
                 """)
print("Table created successfully")
