from PyQt6.QtWidgets import QPushButton, QMenu
from PyQt6.QtGui import QFont, QFontDatabase, QAction
from ui.themes.default_theme import def_theme
from ui.themes.northern_lights_theme import northern_theme

def change_theme_button(self):
    QFontDatabase.addApplicationFont(r"files\fonts\Assistant-VariableFont_wght.ttf")
    font = QFont("Assistant Light", 20)
    
    self.change_theme = QPushButton("Change theme", self)
    self.change_theme.resize(150, 55)
    self.change_theme.move(20, 370)
    self.change_theme.setFont(font)
    self.change_theme.setStyleSheet("QPushButton {font-size: 20px; background-color: #2E2E2E; border-radius: 8px;} QPushButton:hover {background-color: #2A2A2A;}")
    
    self.change_theme.clicked.connect(lambda: show_menu(self))
 
    
def show_menu(self):
    menu = QMenu(self)
    menu.setStyleSheet("""
        QMenu {
            background-color: #212121;
            border: 1px solid #2E2E2E;
        }
        QMenu::item {
            background-color: #212121;
            color: white;
        }
        QMenu::item:selected {
            background-color: #4A4A4A;
        }
    """)
    
    default_theme_button = QAction("Default", self)
    sea_blue_theme_button = QAction("Northern lights", self)
    menu.addAction(default_theme_button)
    menu.addAction(sea_blue_theme_button)

    default_theme_button.triggered.connect(lambda: def_theme(self))
    sea_blue_theme_button.triggered.connect(lambda: northern_theme(self))
    
    menu.exec(self.change_theme.mapToGlobal(self.change_theme.rect().bottomLeft()))
    