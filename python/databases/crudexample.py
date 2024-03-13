# when working with sqlite3 import the package 
import sqlite3

# first create the database  
# storing reference = variable 
conn = sqlite3.connect('moringa.db')

# Creating our tables 
# students 
# tms 
# tms_students 
# the execute command allows us to execute the SQL queries to our SQL engine
conn.execute('''CREATE TABLE IF NOT EXISTS students(
             id INTEGER PRIMARY KEY,
             name VARCHAR NOT NULL, 
             email TEXT NULL
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS tms(
             id INTEGER PRIMARY KEY,
             name VARCHAR NOT NULL, 
             email TEXT NULL,
             staffnumber INTEGER NOT NULL
);''')


conn.execute('''CREATE TABLE IF NOT EXISTS tms_students(
             id INTEGER PRIMARY KEY,
             tmsid INTEGER, 
             studentid INTEGER, 
             FOREIGN KEY(tmsid) REFERENCES tms(id),
             FOREIGN KEY(studentid) REFERENCES students(id)
);''')

# CRUD 
name = "Mary"
email = "mary@moringaschool.com"

# CREATE A RECORD 
# INSERT QUERY is used to insert records to a DB table 
# Prepared statements : sql injections :: what is this ?? 
# before inserting a record check for the presence of the record 
#  create a cursor object to access query methods from the sqlite package 
cursor = conn.cursor()
cursor.execute("SELECT id FROM students WHERE name = ? AND email = ?", (name, email))
existing_record = cursor.fetchone()

if not existing_record:
    conn.execute("INSERT INTO students (name, email) VALUES (?,?)", (name, email))
else: 
    print("record already exists")


# READ A RECORD 
# SELECT namecolumn1, namecolumn2 FROM tablename 
# SELECT * FROM tablename
# SELECT : returns the records as a list (array)
result = conn.execute("SELECT * FROM students")
# loop to see data 
for row in result:
    print(f" id: {row[0]} , Name: {row[1]} , Email: {row[2]}")

# to update : "UPDATE tablename SET fieldname = ?, fieldname= ? WHERE id = ?", (values,?)
conn.execute("UPDATE students SET name = ? WHERE id = ?", ("Bill", 1))

# to Delete : DELETE FROM tablename 
# DELETE FROM tablename WHERE fieldname = ? , (2,)
conn.execute("DELETE FROM students WHERE id = ?", (2,))

# commit the changes 
conn.commit()

#close the connection 
conn.close()