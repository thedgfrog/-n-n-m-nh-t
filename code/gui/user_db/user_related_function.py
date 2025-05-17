import sqlite3
import re
import hashlib
from main import run_all_game

def user_exists(username):
    with sqlite3.connect('user_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone() is not None

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username, password, email):
    if user_exists(username):
        return "Tên người dùng đã tồn tại."
    if not is_valid_email(email):
        return "Email không đúng định dạng."
    hashed_pass = hash_password(password)
    try:
        with sqlite3.connect('user_system.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                           (username, hashed_pass, email))
            conn.commit()
        
        return "Đăng ký thành công!"
    except Exception as e:
        return f"Đăng ký thất bại: {str(e)}"

def confirm_login(username, password):
    hashed_pass = hash_password(password)
    with sqlite3.connect('user_system.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_pass))
        user = cursor.fetchone()
    
    if user:
        return True, "Đăng nhập thành công!"
    else:
        return False, "Sai tên đăng nhập hoặc mật khẩu."