from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont, QFontDatabase

def reset_all_button(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    self.reset_button = QPushButton("Reset all", self)
    self.reset_button.resize(220, 60)
    self.reset_button.move(280, 465)
    self.reset_button.setFont(font)
    self.reset_button.setStyleSheet("QPushButton {font-size: 33px; background-color: #2E2E2E; border-radius: 8px;} QPushButton:hover {background-color: #2A2A2A;}")
    
    self.reset_button.clicked.connect(lambda: reset_all_settings(self))
    
    
def reset_all_settings(self):
    self.enter_description_text.setText("")
    self.enter_main_text.setText("")
    self.enter_code.setText("")
    self.enter_tries.setText("")
    self.enter_hour_time_out.setText("")
    self.enter_minutes_time_out.setText("")