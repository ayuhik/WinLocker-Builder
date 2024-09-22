from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont, QFontDatabase
from ui.about_program_window import show_text_widgets

def about_us(self):
    QFontDatabase.addApplicationFont(r"files/fonts/Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    self.about_button = QPushButton("About program", self)
    self.about_button.resize(345, 55)
    self.about_button.move(185, 370)
    self.about_button.setFont(font)
    self.about_button.setStyleSheet("QPushButton {font-size: 25px; background-color: #2E2E2E; border-radius: 8px;} QPushButton:hover {background-color: #2A2A2A;}")
    self.about_button.clicked.connect(lambda: show_text_widgets(self))