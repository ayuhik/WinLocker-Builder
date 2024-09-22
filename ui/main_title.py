from PyQt6.QtWidgets import QLabel, QLineEdit
from PyQt6.QtGui import QFontDatabase, QFont

def main_title_of_winlocker(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    main_title_frame = QLabel(self)
    main_title_frame.setStyleSheet("background-color: #2E2E2E; border-radius: 8px;")
    main_title_frame.resize(510, 70)
    main_title_frame.move(20, 85)
        
    main_title_text = QLabel("Main title", self)
    main_title_text.setStyleSheet("font-size: 18px; background-color: #2E2E2E;")
    main_title_text.setFont(font)
    main_title_text.resize(75, 30)
    main_title_text.move(30, 85)
            
    enter_main_text = QLineEdit(self)
    enter_main_text.setPlaceholderText("Enter the title")
    enter_main_text.setStyleSheet("font-size: 15px; border: 1px solid #1C1C1C; border-radius: 3px;")
    enter_main_text.setFont(font)
    enter_main_text.resize(490, 30)
    enter_main_text.move(30, 115)
    
    return main_title_frame, main_title_text, enter_main_text