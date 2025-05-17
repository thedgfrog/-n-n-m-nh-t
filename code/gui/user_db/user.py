import sqlite3

# Kết nối (tự động tạo file database nếu chưa có)
conn = sqlite3.connect('user_system.db')
cursor = conn.cursor()

# Tạo bảng người dùng (dùng cho cả đăng ký và đăng nhập)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT
)
''')

# Tạo bảng lịch sử đăng nhập (có thể dùng thêm)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS login_logs (
#     log_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER,
#     login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY(user_id) REFERENCES users(id)
# )
# ''')

conn.commit()
conn.close()
print("Đã tạo bảng thành công.")