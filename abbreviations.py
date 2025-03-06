
import streamlit as st
import sqlite3

# 📌 Function to connect to the database
def connect_db():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()

        # Ensure the abbreviations table exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS abbreviations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            abbreviation TEXT UNIQUE,
                            meaning TEXT,
                            words TEXT)''')
        conn.commit()

# 📌 Function to fetch abbreviations from the database
def fetch_abbreviations():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT abbreviation, meaning, words FROM abbreviations")
        return cursor.fetchall()

# 📌 Function to display the abbreviations page in Streamlit
def show_abbreviations_page():
    st.title("📖 Abbreviations Dictionary")

    data = fetch_abbreviations()

    if not data:
        st.warning("No abbreviations found in the database.")
    else:
        for abbr, meaning, words in data:
            st.write(f"**{abbr}**: {meaning} (_{words}_)")

# ✅ Ensure the function is at the bottom for import
if __name__ == "__main__":
    connect_db()
    show_abbreviations_page()
