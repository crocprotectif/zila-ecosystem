import sqlite3

def init_db():
    conn = sqlite3.connect("zila.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        address TEXT,
        private_key TEXT,
        pin TEXT,
        balance REAL DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def save_user(user_id, address, pk):
    conn = sqlite3.connect("zila.db")
    c = conn.cursor()

    c.execute("INSERT OR REPLACE INTO users (user_id,address,private_key) VALUES (?,?,?)",
              (user_id,address,pk))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("zila.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    data = c.fetchone()
    conn.close()
    return data

def set_pin(user_id, pin):
    conn = sqlite3.connect("zila.db")
    c = conn.cursor()
    c.execute("UPDATE users SET pin=? WHERE user_id=?", (pin,user_id))
    conn.commit()
    conn.close()
