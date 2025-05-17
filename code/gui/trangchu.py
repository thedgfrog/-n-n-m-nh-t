from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import os

# Thêm đường dẫn để import main.py
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from main import run_all_game

# Giả sử bạn có hàm confirm_login trong user_related_function
from user_db.user_related_function import confirm_login

class PUBGLoginUI(QWidget):
    def __init__(self, switch_to_signup_callback):
        super().__init__()
        self.setWindowTitle("PUBG Login Clone - PyQt5")
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.switch_to_signup_callback = switch_to_signup_callback
        self.init_ui()

    def init_ui(self):
        title = QLabel("PUBG LOGIN")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #f0c420;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        login_button = QPushButton("Login")
        login_button.setCursor(Qt.PointingHandCursor)
        login_button.clicked.connect(self.handle_login)
        login_button.setStyleSheet("""
            background-color: #f0c420;
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        """)

        signup_button = QPushButton("Sign Up")
        signup_button.setCursor(Qt.PointingHandCursor)
        signup_button.setStyleSheet("""
            background-color: #2a2a2a;
            color: white;
            padding: 10px;
            border-radius: 10px;
        """)
        signup_button.clicked.connect(self.switch_to_signup_callback)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.addWidget(title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addWidget(signup_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        success, message = confirm_login(username, password)
        if success:
            QMessageBox.information(self, "Thành công", message)
            self.hide()
            run_all_game()  # Chạy game
        else:
            QMessageBox.critical(self, "Thất bại", message)
            self.username_input.clear()
            self.password_input.clear()


