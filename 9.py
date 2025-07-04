import sqlite3 
connection=sqlite3.connect("student.db")
curs=connection.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER, name TEXT, marks INTEGER)")

curs.execute("INSERT INTO student VALUES (1, 'Gursimran', 90)")
curs.execute("INSERT INTO student VALUES (2, 'Aman', 85)") 

curs.execute("SELECT * FROM student")
data = curs.fetchall()
for rows in data:
    print(data)
connection.commit()
connection.close()
