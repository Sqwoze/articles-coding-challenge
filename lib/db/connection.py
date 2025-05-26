import sqlite3
def get_connection():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
        