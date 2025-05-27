from PySide6.QtWidgets import QPushButton
from consts import MEDIUM_FONT

class Button(QPushButton):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        self.setFont(font)
        self.setProperty('cssClass', 'specialButton')
