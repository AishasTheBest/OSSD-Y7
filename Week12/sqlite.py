import sqlite3

con = sqlite3.connect("project.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")

con.commit()
con.close()

print("Table created successfully!")



