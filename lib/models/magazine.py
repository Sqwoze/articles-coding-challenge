import sqlite3
def create_magazine_table():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()

    conn.execute(''' CREATE TABLE IF NOT EXISTS magazines (
                 id INTEGER PRIMARY KEY,
                 name VARCHAR (255) NOT NULL) ''')
    
    try:
        cursor.execute("ALTER TABLE magazines ADD COLUMN category VARCHAR(255) NOT NULL DEFAULT 'Uncategorized'")
    except sqlite3.OperationalError as e:
        print("Column might already exist:", e)
    

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_magazine_table()
    print("Authors table created successfully!")