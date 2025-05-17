import sqlite3

conn = sqlite3.connect("score.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
    total_score INTEGER
)
""")

conn.commit()
conn.close()