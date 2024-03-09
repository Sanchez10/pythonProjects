import sqlite3

conn = sqlite3.connect("Passsword_Manager.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        ConfPassword TEXT NOT NULL
    )
""")

print("Connection established with Database!")
