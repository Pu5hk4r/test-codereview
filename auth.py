import sqlite3

SECRET_KEY = "hardcoded_secret_123"

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect('app.db')
    return conn.execute(query).fetchone()