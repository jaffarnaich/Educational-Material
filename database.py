import sqlite3
import pandas as pd

# 📌 Function to connect to SQLite3 database and create tables
def connect_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Creating necessary tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS idioms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        phrase TEXT UNIQUE,
                        meaning TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS abbreviations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        abbreviation TEXT UNIQUE,
                        meaning TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT,
                        message TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS quiz_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user TEXT NOT NULL,
                        score INTEGER NOT NULL,
                        total_questions INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS user_inputs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        input_text TEXT NOT NULL)''')

    conn.commit()
    conn.close()
    print("✅ Database setup completed successfully!")

# 📌 Function to insert data into specified tables
def insert_data(table, data):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        if table == "idioms":
            cursor.execute("INSERT INTO idioms (phrase, meaning) VALUES (?, ?)", data)
        elif table == "abbreviations":
            cursor.execute("INSERT INTO abbreviations (abbreviation, meaning) VALUES (?, ?)", data)
        elif table == "feedback":
            cursor.execute("INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)", data)
        elif table == "user_inputs":
            cursor.execute("INSERT INTO user_inputs (input_text) VALUES (?)", (data,))
        else:
            print("❌ Invalid table name provided!")
            return
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"⚠ Data already exists in the {table} table.")
    finally:
        conn.close()

# 📌 Function to get data from specified tables
def get_data(table):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()
    conn.close()
    return data

# 📌 Function to insert quiz results
def insert_quiz_result(user, score, total_questions):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quiz_results (user, score, total_questions) VALUES (?, ?, ?)", 
                   (user, score, total_questions))
    conn.commit()
    conn.close()

# 📌 Function to fetch quiz results
def fetch_quiz_results():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quiz_results")
    data = cursor.fetchall()
    conn.close()
    return data

# 📌 Function to insert user input into the database
def insert_user_input(user_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_inputs (input_text) VALUES (?)", (user_input,))
    conn.commit()
    conn.close()

# 📌 Function to fetch user inputs
def fetch_user_inputs():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_inputs")
    data = cursor.fetchall()
    conn.close()
    return data

# 📌 Initialize the database when the script runs
if __name__ == "__main__":
    connect_db()
