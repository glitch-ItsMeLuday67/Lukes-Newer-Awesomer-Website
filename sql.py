from os import close
import sqlite3
conn=sqlite3.connect('Students.db')
cur=conn.cursor()
# cur.execute('CREATE TABLE Students_Record(Roll_No INTEGER PRIMARY KEY, Student_Name TEXT, Age INTEGER);')
# print("Table Created")
# cur.execute('INSERT INTO Students_Record Values(1, "Johny", 10);')
# cur.execute('INSERT INTO Students_Record Values(2, "Manish", 13);')
# cur.execute('INSERT INTO Students_Record Values(3, "Saniya", 15);')
records = cur.execute('SELECT Roll_No FROM Students_Record;').fetchall()
# cur.execute('''CREATE TABLE registration_db
#     (Username TEXT PRIMARY KEY,
#     Password TEXT,
#     Email TEXT);''')
cur.execute("DROP TABLE registration_db")
print("Table deleted")
for record in records:
    print(record[0])
conn.commit()
# print("Values inserted")
conn.close()