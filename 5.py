import sqlite3
import pandas as pd

conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, age INT, grade FLOAT)')

students = [
    ('Kew1', 20, 85.5),
    ('Kew2', 19, 92.0),
    ('Kew3', 21, 78.5),
    ('Kew4', 20, 88.0),
    ('Kew5', 19, 90.5)
]

cur.executemany('INSERT INTO students VALUES (?,?,?)', students)
conn.commit()
df = pd.read_sql_query('SELECT * FROM students', conn)

filtered = df[df['age'] > 19]
avg_grade = df['grade'].mean()
sorted_df = df.sort_values('grade', ascending=False)
age_groups = df.groupby('age').count()
highest_grade = df['grade'].max()

print(df)
print('\nFiltered ages > 19:\n', filtered)
print('\nAverage grade:', avg_grade)
print('\nSorted by grade:\n', sorted_df)
print('\nAge groups:\n', age_groups)
print('\nHighest grade:', highest_grade)
conn.close()