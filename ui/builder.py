from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont, QFontDatabase
from builder.build import build_text

def builder_button(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    self.build_button = QPushButton("Build", self)
    self.build_button.resize(240, 60)
    self.build_button.move(20, 465)
    self.build_button.setFont(font)
    self.build_button.setStyleSheet("QPushButton {font-size: 33px; background-color: #2E2E2E; border-radius: 8px;} QPushButton:hover {background-color: #2A2A2A;}")
    self.build_button.clicked.connect(lambda: create_build(self))
    
    
def create_build(self):
    self.main_text = self.enter_main_text.text()
    self.description_text = self.enter_description_text.toPlainText()
    self.pincode_text = self.enter_code.text()
    self.tries_text = self.enter_tries.text()
    self.hour_text = self.enter_hour_time_out.text()
    self.minutes_text = self.enter_minutes_time_out.text()
    self.code = build_text(self.main_text, self.description_text, self.pincode_text, self.tries_text, self.hour_text, self.minutes_text)
    
    with open("build.py", "w", encoding="utf-8") as file:
        file.write(self.code)
