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
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if button_text not in "0123456789.":
                    button.setProperty("cssClass", "specialButton")
                self.addWidget(button, row_number, column_number)
