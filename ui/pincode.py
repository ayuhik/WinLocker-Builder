from PyQt6.QtWidgets import QLabel, QLineEdit
from PyQt6.QtGui import QFontDatabase, QFont

def code_of_winlocker(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
        
    code_frame = QLabel(self)
    code_frame.setStyleSheet("background-color: #2E2E2E; border-radius: 8px;")
    code_frame.resize(150, 55)
    code_frame.move(20, 270)
        
    code_text = QLabel("Code", self)
    code_text.setStyleSheet("font-size: 15px; background-color: #2E2E2E;")
    code_text.setFont(font)
    code_text.resize(75, 25)
    code_text.move(30, 270)
        
    enter_code = QLineEdit(self)
    enter_code.setPlaceholderText("Enter the code")
    enter_code.setStyleSheet("font-size: 12px; border: 1px solid #1c1c1c; border-radius: 3px;")
    enter_code.setFont(font)
    enter_code.resize(135, 22)
    enter_code.move(27, 297)
    
    return code_frame, code_text, enter_code