from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFrame, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from user_db.user_related_function import register_user

class PUBGSignupUI(QWidget):
    def __init__(self, switch_to_login_callback):
        super().__init__()
        self.setWindowTitle("PUBG Sign Up Clone - PyQt5")
        self.setFixedSize(500, 400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.switch_to_login_callback = switch_to_login_callback
        self.init_ui()

    def init_ui(self):
        title = QLabel("PUBG SIGN UP")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #f0c420;")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")
        self.username_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email")
        self.email_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Create a password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Re-enter your password")
        self.confirm_input.setEchoMode(QLineEdit.Password)
        self.confirm_input.setStyleSheet("padding: 10px; border-radius: 5px;")

        signup_button = QPushButton("Create Account")
        signup_button.setCursor(Qt.PointingHandCursor)
        signup_button.setStyleSheet("""
            background-color: #f0c420;
            color: black;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        """)

        back_login_button = QPushButton("Back to Login")
        back_login_button.setCursor(Qt.PointingHandCursor)
        back_login_button.setStyleSheet("""
            background-color: #2a2a2a;
            color: white;
            padding: 10px;
            border-radius: 10px;
        """)
        back_login_button.clicked.connect(self.switch_to_login_callback)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.addWidget(title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_input)
        layout.addWidget(signup_button)
        layout.addWidget(QFrame())  # Spacer
        layout.addWidget(back_login_button)

        self.setLayout(layout)

        signup_button.clicked.connect(self.handle_signup)

    def handle_signup(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm = self.confirm_input.text()

        if not username or not email or not password or not confirm:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập đầy đủ thông tin.")
            return

        if password != confirm:
            QMessageBox.warning(self, "Thông báo", "Mật khẩu nhập lại không khớp.")
            return

        result = register_user(username, password, email)
        if "thành công" in result.lower():
            QMessageBox.information(self, "Thông báo", result)
            self.switch_to_login_callback()  # Chuyển về màn hình đăng nhập nếu muốn
        else:
            QMessageBox.critical(self, "Lỗi", result)
            self.password_input.clear()
            self.username_input.clear()
            self.email_input.clear()
