from os import close
import sqlite3
conn=sqlite3.connect('users.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE registration_db
    (Username TEXT PRIMARY KEY,
    Password TEXT,
    Email TEXT);''')
records = cur.execute('SELECT Username FROM registration_db;').fetchall()
# cur.execute("DROP TABLE registration_db")
# print("Table deleted")
for record in records:
    print(record[0])
conn.commit()
print("Values inserted")
conn.close()