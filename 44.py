import sqlite3

conn=sqlite3.connect('Employee.db')

cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Employees(
    name VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    salary INT
);''')

conn.commit()

def Add_Employee(name, phone_number, email, salary):
    conn=sqlite3.connect('Employee.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO Employees (name, phone_number, email, salary) VALUES(?,?,?,?)',(name, phone_number, email, salary))
    conn.commit

def Change_Atrib(name, phone_number, email, salary):
    conn=sqlite3.connect('Employees.db')
    cur=conn.cursor()
    cur.execute('UPDATE Employees phone_number=?, email=?, salary=? WHERE name=?',( phone_number, email, salary, name))
    conn.commit

def Delete_Employee(name):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE name=?', (name,))
    conn.commit()

def Select_By_Name(name):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Empoloyees WHERE name=?',(name))
