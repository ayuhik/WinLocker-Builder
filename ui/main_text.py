from PyQt6.QtWidgets import QLabel, QTextEdit
from PyQt6.QtGui import QFontDatabase, QFont

def main_text_of_winlocker(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    main_text_frame = QLabel(self)
    main_text_frame.setStyleSheet("background-color: #2E2E2E; border-radius: 8px;")
    main_text_frame.resize(510, 90)
    main_text_frame.move(20, 170)
        
    main_text = QLabel("Text description", self)
    main_text.setStyleSheet("font-size: 18px; background-color: #2E2E2E;")
    main_text.setFont(font)
    main_text.resize(175, 30)
    main_text.move(30, 170)
        
    enter_description_text = QTextEdit(self)
    enter_description_text.setPlaceholderText("Enter the description")
    enter_description_text.setStyleSheet("font-size: 15px; border: 1px solid #1c1c1c; border-radius: 3px;")
    enter_description_text.setFont(font)
    enter_description_text.resize(490, 50)
    enter_description_text.move(30, 200)
    
    return main_text_frame, main_text, enter_description_text