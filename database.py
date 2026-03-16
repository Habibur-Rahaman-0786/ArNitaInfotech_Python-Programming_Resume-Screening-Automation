import sqlite3

#Function to create a database
def create_database():
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS candidates(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   phone TEXT,
                   skills TEXT,
                   score REAL
                   )
                   """)
    
    conn.commit()
    conn.close()

#Function to Insert values in Database
def insert_candidate(name, email, skills, phone, score):
    conn = sqlite3.connect("candidates.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO candidates(name, email, phone, skills, score)
                   VALUES (?, ?, ?, ?, ?)
                   """, (name, email, phone, skills, score))
    
    conn.commit()
    conn.close()