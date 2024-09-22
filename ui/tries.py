from PyQt6.QtWidgets import QLineEdit, QLabel
from PyQt6.QtGui import QFontDatabase, QFont, QIntValidator

def tries_of_winlocker(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    tries_frame = QLabel(self)
    tries_frame.setStyleSheet("background-color: #2E2E2E; border-radius: 8px;")
    tries_frame.resize(150, 55)
    tries_frame.move(185, 270)
        
    tries_text = QLabel("Tries", self)
    tries_text.setStyleSheet("font-size: 15px; background-color: #2E2E2E;")
    tries_text.setFont(font)
    tries_text.resize(75, 25)
    tries_text.move(192, 270)
            
    self.enter_tries = QLineEdit(self)
    self.enter_tries.setPlaceholderText("Enter the tries")
    self.enter_tries.setStyleSheet("font-size: 12px; border: 1px solid #1c1c1c; border-radius: 3px;")
    self.enter_tries.setFont(font)
    self.enter_tries.resize(135, 22)
    self.enter_tries.move(192, 297)
    self.enter_tries.setValidator(QIntValidator(1, 9999))
    
    self.enter_tries.textChanged.connect(
        lambda: self.enter_tries.setText("1") if self.enter_tries.text() == "0" else None
    )
    
    return tries_frame, tries_text