# import sys
# import sqlite3
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
# from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
# from PyQt5.QtCore import Qt

# # ===== DATABASE FUNCTIONS =====

# def save_score_to_db(total_score):
#     try:
#         conn = sqlite3.connect("score.db")
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS game_sessions (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
#                 total_score INTEGER
#             )
#         ''')
#         cursor.execute("INSERT INTO game_sessions (total_score) VALUES (?)", (total_score,))
#         conn.commit()
#         conn.close()
#     except Exception as e:
#         print("Lỗi khi lưu điểm:", e)

# def get_highest_score():
#     try:
#         conn = sqlite3.connect("score.db")
#         cursor = conn.cursor()
#         cursor.execute("SELECT MAX(total_score) FROM game_sessions")
#         result = cursor.fetchone()
#         conn.close()
#         return result[0] if result and result[0] is not None else 0
#     except Exception as e:
#         print("Lỗi khi lấy điểm cao nhất:", e)
#         return 0

# # ===== GUI CLASS =====

# class EndingScreen(QWidget):
#     def __init__(self, score=0):
#         super().__init__()
#         self.setWindowTitle("Game Over")
#         self.setFixedSize(600, 400)

#         self.set_background("D:/PyGame/hunter/images/ending_background.jpg")

#         highest = get_highest_score()

#         main_layout = QVBoxLayout()
#         main_layout.setAlignment(Qt.AlignCenter)

#         # GAME OVER
#         title = QLabel("GAME OVER")
#         title.setFont(QFont("Arial", 32, QFont.Bold))
#         title.setStyleSheet("color: red;")
#         title.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(title)

#         # PLAY AGAIN?
#         question = QLabel("PLAY AGAIN?")
#         question.setFont(QFont("Arial", 16))
#         question.setStyleSheet("color: white;")
#         question.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(question)

#         # Score display
#         score_layout = QHBoxLayout()
#         score_layout.setAlignment(Qt.AlignCenter)

#         score_label = QLabel(f"Your Score: {score}")
#         score_label.setFont(QFont("Arial", 14))
#         score_label.setStyleSheet("color: yellow;")

#         highest_label = QLabel(f"Highest: {highest}")
#         highest_label.setFont(QFont("Arial", 14))
#         highest_label.setStyleSheet("color: cyan;")

#         score_layout.addWidget(score_label)
#         score_layout.addWidget(highest_label)
#         main_layout.addLayout(score_layout)

#         # Buttons
#         btn_layout = QHBoxLayout()
#         btn_yes = QPushButton("YES")
#         btn_no = QPushButton("NO")
#         for btn in (btn_yes, btn_no):
#             btn.setFixedSize(100, 40)
#             btn.setStyleSheet("""
#                 QPushButton {
#                     background-color: white;
#                     color: black;
#                     font-weight: bold;
#                     border: 2px solid black;
#                     border-radius: 5px;
#                 }
#                 QPushButton:hover {
#                     background-color: lightgray;
#                 }
#             """)
#         btn_layout.addWidget(btn_yes)
#         btn_layout.addWidget(btn_no)
#         main_layout.addLayout(btn_layout)

#         self.setLayout(main_layout)

#     def set_background(self, image_path):
#         background = QPixmap(image_path)
#         palette = QPalette()
#         palette.setBrush(QPalette.Window, QBrush(background.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
#         self.setPalette(palette)

# # ===== SHOW FUNCTION =====

# # def show_ending_screen(score):
# #     save_score_to_db(score)
# #     app = QApplication.instance()
# #     if app is None:
# #         app = QApplication(sys.argv)
# #     screen = EndingScreen(score)
# #     screen.show()
# #     app.exec_()
# def show_ending_screen(score):
#     from PyQt5.QtWidgets import QApplication
#     app = QApplication.instance()

#     if app is None:
#         print("No QApplication instance running. Cannot show ending screen.")
#         return

#     screen = EndingScreen(score)
#     screen.show()

# # ===== TEST =====


import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt

# ===== DATABASE FUNCTIONS =====

def save_score_to_db(total_score):
    try:
        conn = sqlite3.connect("score.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                total_score INTEGER
            )
        ''')
        cursor.execute("INSERT INTO game_sessions (total_score) VALUES (?)", (total_score,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("Lỗi khi lưu điểm:", e)

def get_highest_score():
    try:
        conn = sqlite3.connect("score.db")
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(total_score) FROM game_sessions")
        result = cursor.fetchone()
        conn.close()
        return result[0] if result and result[0] is not None else 0
    except Exception as e:
        print("Lỗi khi lấy điểm cao nhất:", e)
        return 0
# hàm thực hiện sự kiện yes no


# ===== GUI CLASS =====

# Biến toàn cục để giữ cửa sổ không bị hủy
ending_screen_instance = None

class EndingScreen(QWidget):
    def __init__(self, score=0):
        super().__init__()
        self.setWindowTitle("Game Over")
        self.setFixedSize(600, 400)

        self.set_background("D:/PyGame/hunter/images/ending_background.jpg")

        highest = get_highest_score()

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # GAME OVER
        title = QLabel("GAME OVER")
        title.setFont(QFont("Arial", 32, QFont.Bold))
        title.setStyleSheet("color: red;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # PLAY AGAIN?
        question = QLabel("PLAY AGAIN?")
        question.setFont(QFont("Arial", 16))
        question.setStyleSheet("color: white;")
        question.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(question)

        # Score display
        score_layout = QHBoxLayout()
        score_layout.setAlignment(Qt.AlignCenter)

        score_label = QLabel(f"Your Score: {score}")
        score_label.setFont(QFont("Arial", 14))
        score_label.setStyleSheet("color: yellow;")

        highest_label = QLabel(f"Highest: {highest}")
        highest_label.setFont(QFont("Arial", 14))
        highest_label.setStyleSheet("color: cyan;")

        score_layout.addWidget(score_label)
        score_layout.addWidget(highest_label)
        main_layout.addLayout(score_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_yes = QPushButton("YES")
        btn_yes.clicked.connect(self.on_yes_clicked)
        btn_no = QPushButton("NO")
        btn_no.clicked.connect(self.on_no_clicked)
        for btn in (btn_yes, btn_no):
            btn.setFixedSize(100, 40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    font-weight: bold;
                    border: 2px solid black;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: lightgray;
                }
            """)
        btn_layout.addWidget(btn_yes)
        btn_layout.addWidget(btn_no)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)
    def on_yes_clicked(self):         # Đóng cửa sổ EndingScreen
        from main import run_all_game       # Chạy lại game
        self.close()
        run_all_game()

    def on_no_clicked(self):
        QApplication.quit()  # Thoát hẳn ứng dụng

    def set_background(self, image_path):
        background = QPixmap(image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setPalette(palette)

# ===== SHOW FUNCTION =====

def show_ending_screen(score):
    global ending_screen_instance
    save_score_to_db(score)
    
    app = QApplication.instance()
    if app is None:
        print("No QApplication instance running. Cannot show ending screen.")
        return

    ending_screen_instance = EndingScreen(score)
    ending_screen_instance.show()
