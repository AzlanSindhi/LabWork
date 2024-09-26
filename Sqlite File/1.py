import sqlite3
import pandas as pd
conn = sqlite3.connect('result.db')
c = conn.cursor()

# c.execute(''' CREATE TABLE Result (
#     s_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     s_name TEXT CHECK (LENGTH(s_name) < 25),
#     sub1 INTEGER CHECK (sub1 >= 0 AND sub1 <= 100),
#     sub2 INTEGER CHECK (sub2 >= 0 AND sub2 <= 100),
#     sub3 INTEGER CHECK (sub3 >= 0 AND sub3 <= 100),
#     sub4 INTEGER CHECK (sub4 >= 0 AND sub4 <= 100),
#     sub5 INTEGER CHECK (sub5 >= 0 AND sub5 <= 100)
# );''')
# c.execute('''INSERT INTO Result (s_name, sub1, sub2, sub3, sub4, sub5) VALUES
# ('Amit', 85, 76, 65, 90, 70),
# ('Bina', 45, 56, 75, 60, 80),
# ('Chetan', 35, 46, 67, 49, 77),
# ('Dinesh', 60, 77, 80, 66, 69),
# ('Esha', 92, 88, 79, 91, 85),
# ('Falguni', 53, 49, 40, 60, 57),
# ('Geeta', 75, 65, 80, 77, 89),
# ('Hiren', 80, 95, 60, 70, 88),
# ('Isha', 44, 50, 55, 48, 60),
# ('Jiten', 90, 85, 78, 88, 95);''')
# c.execute('''
# SELECT s_name, 
#        (sub1 + sub2 + sub3 + sub4 + sub5) AS total, 
#        ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 AS percentage,
#        CASE
#            WHEN sub1 < 35 OR sub2 < 35 OR sub3 < 35 OR sub4 < 35 OR sub5 < 35 THEN 'Fail'
#            WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 80 THEN 'A+'
#            WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 70 THEN 'A'
#            WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 60 THEN 'B'
#            WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 50 THEN 'C'
#            ELSE 'Pass'
#        END AS grade
# FROM Result
# ORDER BY grade;''')

result = pd.read_sql_query('''SELECT s_name, 
       (sub1 + sub2 + sub3 + sub4 + sub5) AS total, 
       ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 AS percentage,
       CASE
           WHEN sub1 < 35 OR sub2 < 35 OR sub3 < 35 OR sub4 < 35 OR sub5 < 35 THEN 'Fail'
           WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 80 THEN 'A+'
           WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 70 THEN 'A'
           WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 60 THEN 'B'
           WHEN ((sub1 + sub2 + sub3 + sub4 + sub5) * 100.0) / 500 >= 50 THEN 'C'
           ELSE 'Pass'
       END AS grade
FROM Result
ORDER BY grade;''', conn)

print(result)
print("Executed successfully")
conn.commit()
conn.close()