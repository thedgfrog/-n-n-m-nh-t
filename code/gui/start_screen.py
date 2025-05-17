import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap

class MainWindow(QWidget):
    def __init__(self, back_to_login_callback=None):
        super().__init__()
        self.setWindowTitle("Background Image with Styled Button")
        self.setFixedSize(500, 400)
        self.back_to_login_callback = back_to_login_callback

        # Layout để canh giữa button
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Tạo nút chính giữa
        btn = QPushButton("Bắt đầu")
        btn.setFixedSize(180, 60)

        # CSS cho nút
        btn.setStyleSheet("""
            QPushButton {
                background-color: #f0c420;
                color: #1e1e1e;
                font-size: 20px;
                font-weight: bold;
                border-radius: 15px;
                padding: 10px;
                border: 3px solid #d4a017;
                box-shadow: 3px 3px 5px rgba(0,0,0,0.3);
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #d4a017;
                color: white;
                border: 3px solid #f0c420;
            }
            QPushButton:pressed {
                background-color: #b2870d;
                border: 3px solid #a0780a;
            }
        """)

        # Kết nối nút với callback nếu có
        if self.back_to_login_callback:
            btn.clicked.connect(self.back_to_login_callback)

        layout.addWidget(btn)
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("images/back.jpg")  # đường dẫn ảnh nền
        painter.drawPixmap(self.rect(), pixmap)  # vẽ ảnh full nền

# Dưới đây để test nếu chạy file này trực tiếp
if __name__ == "__main__":
    def dummy_callback():
        print("Back to login clicked!")

    app = QApplication(sys.argv)
    window = MainWindow(dummy_callback)
    window.show()
    sys.exit(app.exec_())
