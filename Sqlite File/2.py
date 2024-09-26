import sqlite3
import pandas as pd

# Create Employee Table and Insert Records
conn = sqlite3.connect('Mydatabase1.db')

# Create Employee table
conn.execute('''
    CREATE TABLE Employee (
        eno INTEGER PRIMARY KEY,
        ename TEXT NOT NULL,
        designation TEXT,
        basic REAL,
        da REAL,
        gross_salary REAL
    )
''')

# Insert five records into Employee table
employees = [
    (1, 'Alice', 'Manager', 30000, 10000, 40000),
    (2, 'Bob', 'Developer', 25000, 8000, 33000),
    (3, 'Charlie', 'Designer', 20000, 7000, 27000),
    (4, 'David', 'Tester', 18000, 5000, 23000),
    (5, 'Eva', 'HR', 22000, 6000, 28000)
]

with conn:
    conn.executemany('INSERT INTO Employee (eno, ename, designation, basic, da, gross_salary) VALUES (?, ?, ?, ?, ?, ?)', employees)

# Load Employee data into a DataFrame
df_employee = pd.read_sql_query('SELECT * FROM Employee', conn)
print("Employee DataFrame:")
print(df_employee)

# Close the connection
conn.close()