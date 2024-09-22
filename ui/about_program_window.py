from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QFontDatabase

check_widgets = None

def about_widgets(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)

    self.about_frame = QLabel(self)
    self.about_frame.resize(700, 700)
    self.about_frame.setStyleSheet("background-color: #1C1C1C;")
    self.about_frame.move(0, 61)
    self.about_frame.hide()
                                     
    self.main_about_frame = QLabel(self)
    self.main_about_frame.resize(530, 400)
    self.main_about_frame.setStyleSheet("font-size: 40px; background-color: #212121; border-radius: 15px;")
    self.main_about_frame.move(10, 70)
    self.main_about_frame.hide()
    
    self.close_button = QPushButton("X", self)
    self.close_button.setStyleSheet("QPushButton {font-size: 25px; background-color: #2E2E2E; border-radius: 8px;} QPushButton:hover {background-color: #2A2A2A;}")
    self.close_button.resize(40, 40)
    self.close_button.move(492, 80)
    self.close_button.hide()
    self.close_button.clicked.connect(lambda: hide_text_widgets(self))

    self.first_text = QLabel("This program is for educational and informational\npurposes only, nothing more. I do not vouch for\nyour actions related to this program, so all\nresponsibility lies with you.", self)
    self.first_text.setStyleSheet("font-size: 23px; background-color: #212121;")
    self.first_text.setFont(font)
    self.first_text.resize(440, 140)
    self.first_text.move(40, 70)
    self.first_text.hide()

    self.second_text = QLabel("This version is in the early stages of\ndevelopment, so there may be bugs and not\nonly. The program is updated regularly, so keep\nan eye out for updates.", self)
    self.second_text.setStyleSheet("font-size: 22px; background-color: #212121;")
    self.second_text.setFont(font)
    self.second_text.resize(440, 140)
    self.second_text.move(40, 320)
    self.second_text.hide()
    
    self.second_about_frame = QLabel(self)
    self.second_about_frame.resize(530, 80)
    self.second_about_frame.setStyleSheet("font-size: 40px; background-color: #212121; border-radius: 15px;")
    self.second_about_frame.move(10, 490)
    self.second_about_frame.hide()
    
    self.telegram_link = QLabel("<a href='https://t.me/argertt'>Telegram</a>", self)
    self.telegram_link.setOpenExternalLinks(True)
    self.telegram_link.setStyleSheet("font-size: 30px; background-color: #212121;")
    self.telegram_link.setFont(font)
    self.telegram_link.resize(120, 40)
    self.telegram_link.move(40, 510)
    self.telegram_link.hide()
    
    self.discord_link = QLabel("<a href='https://discordapp.com/users/1284925895659884594'>Discord</a>", self)
    self.discord_link.setOpenExternalLinks(True)
    self.discord_link.setStyleSheet("font-size: 30px; background-color: #212121;")
    self.discord_link.setFont(font)
    self.discord_link.resize(120, 40)
    self.discord_link.move(170, 510)
    self.discord_link.hide()
    
    self.github_link = QLabel("<a href='https://github.com/ayuhik'>Github</a>", self)
    self.github_link.setOpenExternalLinks(True)
    self.github_link.setStyleSheet("font-size: 30px; background-color: #212121;")
    self.github_link.setFont(font)
    self.github_link.resize(120, 40)
    self.github_link.move(280, 510)
    self.github_link.hide()
    
    
def show_text_widgets(self):
    self.about_frame.show()
    self.main_about_frame.show()
    self.close_button.show()
    self.first_text.show()
    self.second_text.show()
    self.second_about_frame.show()
    self.telegram_link.show()
    self.discord_link.show()
    self.github_link.show()


def hide_text_widgets(self):
    self.about_frame.hide()
    self.main_about_frame.hide()
    self.close_button.hide()
    self.first_text.hide()
    self.second_text.hide()
    self.second_about_frame.hide()
    self.telegram_link.hide()
    self.discord_link.hide()
    self.github_link.hide()