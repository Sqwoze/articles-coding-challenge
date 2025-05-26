import sqlite3
def create_authors_table():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()

    conn.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name VARCHAR (255) NOT NULL)''')


    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_authors_table()
    print("Authors table created successfully!")