from consts import MEDIUM_FONT
from PySide6.QtWidgets import QGridLayout, QPushButton


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        self.setFont(font)
        self.setProperty("cssClass", "specialButton")


class ButtonGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]
        self._makeGrid()

    def _makeGrid(self):
        for row_number, row in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row):
                print("Linha", row_number, "Coluna", column_number, "Text", button_text)
