import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from trangchu import PUBGLoginUI
from signup import PUBGSignupUI
from start_screen import MainWindow
from PyQt5.QtGui import QIcon

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_ui = PUBGLoginUI(self.show_signup)
        self.signup_ui = PUBGSignupUI(self.show_login)
        self.start_ui = MainWindow(self.show_login)
        
        self.setWindowIcon(QIcon("images/hunter (1).png"))

        self.addWidget(self.login_ui)   # index 0
        self.addWidget(self.signup_ui)  # index 1
        self.addWidget(self.start_ui)   # index 2

        self.setCurrentIndex(2)  # Bắt đầu từ start screen
        self.setWindowTitle("PUBG Login / Signup")

    def show_signup(self):
        self.setCurrentIndex(1)  # Chuyển sang trang đăng ký

    def show_login(self):
        self.setCurrentIndex(0)  # Chuyển về trang đăng nhập

    def show_start_screen(self):
        self.setCurrentIndex(2)  # Chuyển sang màn hình start screen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
