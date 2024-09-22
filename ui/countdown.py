from PyQt6.QtWidgets import QLabel, QLineEdit
from PyQt6.QtGui import QFontDatabase, QFont, QIntValidator

def timeout_of_winlocker(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    countdown_frame = QLabel(self)
    countdown_frame.setStyleSheet("background-color: #2E2E2E; border-radius: 8px;")
    countdown_frame.resize(95, 55)
    countdown_frame.move(350, 270)
        
    countdown_text = QLabel("Countdown", self)
    countdown_text.setStyleSheet("font-size: 15px; background-color: #2E2E2E;")
    countdown_text.setFont(font)
    countdown_text.resize(75, 25)
    countdown_text.move(357, 270)

    enter_hour_time_out = QLineEdit(self)
    enter_hour_time_out.setPlaceholderText("Hours")
    enter_hour_time_out.setStyleSheet("font-size: 12px; border: 1px solid #1C1C1C; border-radius: 3px;")
    enter_hour_time_out.resize(20, 22)
    enter_hour_time_out.move(357, 297)
    enter_hour_time_out.setValidator(QIntValidator(0, 24))

    hour_timer = QLabel("H", self)
    hour_timer.setStyleSheet("font-size: 15px; background-color: #2E2E2E;")
    hour_timer.setFont(font)
    hour_timer.resize(20, 25)
    hour_timer.move(380, 295)

    enter_minutes_time_out = QLineEdit(self)
    enter_minutes_time_out.setPlaceholderText("Minutes")
    enter_minutes_time_out.setStyleSheet("font-size: 12px; border: 1px solid #1C1C1C; border-radius: 3px;")
    enter_minutes_time_out.resize(20, 22)
    enter_minutes_time_out.move(397, 297)
    enter_minutes_time_out.setValidator(QIntValidator(0, 59))

    minutes_timer = QLabel("M", self)
    minutes_timer.setStyleSheet("font-size: 15px; background-color: #2E2E2E;")
    minutes_timer.setFont(font)
    minutes_timer.resize(20, 25)
    minutes_timer.move(420, 295)


    def validate_hour():
        if enter_hour_time_out.text().isdigit():
            value = int(enter_hour_time_out.text())
            if value > 24:
                enter_hour_time_out.setText("24")
            elif value == 0:
                enter_hour_time_out.setText("0")


    def validate_minutes():
        if enter_minutes_time_out.text().isdigit():
            value = int(enter_minutes_time_out.text())
            if value > 59:
                enter_minutes_time_out.setText("59")
            elif value == 0:
                enter_minutes_time_out.setText("0")
                
                
    enter_hour_time_out.textChanged.connect(validate_hour)
    enter_minutes_time_out.textChanged.connect(validate_minutes)


    return countdown_frame, countdown_text, hour_timer, minutes_timer, enter_hour_time_out, enter_minutes_time_out