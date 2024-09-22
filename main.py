import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFontDatabase, QFont, QIcon
from ui.main_title import main_title_of_winlocker
from ui.main_text import main_text_of_winlocker
from ui.pincode import code_of_winlocker
from ui.tries import tries_of_winlocker
from ui.countdown import timeout_of_winlocker
from ui.change_theme import change_theme_button
from ui.reset_all import reset_all_button
from ui.about_program import about_us
from ui.about_program_window import about_widgets
from ui.builder import builder_button

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WinBuilder")
        self.setFixedSize(550, 590)
        self.setWindowIcon(QIcon(r"files\icons\logo.png"))

        self.setStyleSheet("background-color: #1C1C1C;")
        
        QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
        self.font = QFont("Assistant Light", 20)
            
        self.title_bar = QLabel(self)
        self.title_bar.setStyleSheet("background-color: #2E2E2E;")
        self.title_bar.resize(750, 60)
        self.title_bar.move(0, 0)
        
        self.winlocker_name = QLabel("WinBuilder 0.0.1", self)
        self.winlocker_name.setStyleSheet("font-size: 40px; background-color: #2E2E2E;")
        self.winlocker_name.setFont(self.font)
        self.winlocker_name.resize(500, 60)
        self.winlocker_name.move(15, 0)

        self.main_frame = QLabel(self)
        self.main_frame.resize(530, 270)
        self.main_frame.setStyleSheet("font-size: 40px; background-color: #212121; border-radius: 15px;")
        self.main_frame.move(10, 70)
        
        self.second_frame = QLabel(self)
        self.second_frame.resize(530, 75)
        self.second_frame.setStyleSheet("font-size: 40px; background-color: #212121; border-radius: 15px;")
        self.second_frame.move(10, 360)
        
        self.third_frame = QLabel(self)
        self.third_frame.resize(530, 80)
        self.third_frame.setStyleSheet("font-size: 40px; background-color: #212121; border-radius: 15px;")
        self.third_frame.move(10, 455)
        
        self.main_title_frame, self.main_title_text, self.enter_main_text = main_title_of_winlocker(self)
        self.main_text_frame, self.main_text, self.enter_description_text = main_text_of_winlocker(self)
        self.code_frame, self.code_text, self.enter_code = code_of_winlocker(self)
        self.tries_frame, self.tries_text = tries_of_winlocker(self)
        self.countdown_frame, self.countdown_text, self.hour_timer, self.minutes_timer, self.enter_hour_time_out, self.enter_minutes_time_out = timeout_of_winlocker(self)
        
        change_theme_button(self)
        about_us(self)
        reset_all_button(self)
        builder_button(self)
        about_widgets(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()