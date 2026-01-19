# 02_sql.py
import sqlite3
import pandas as pd

# Create demo DB and table
conn = sqlite3.connect("demo.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, marks INTEGER)")
cur.execute("DELETE FROM students")
cur.executemany(
    "INSERT INTO students VALUES (?, ?, ?)",
    [(1, "Akash", 85), (2, "Rita", 92), (3, "John", 76)]
)
conn.commit()

# Read using pandas
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)

conn.close()
