import sqlite3
conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute('CREATE TABLE students(StudentID INTEGER PRIMARY KEY, Name TEXT, Scores INTEGER, Age INTEGER);')
print('Table is created')
conn.commit()
conn.close()