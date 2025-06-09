from consts import MEDIUM_FONT
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from style.display import Display, Info
from utils import isEmpty, isNumOrDot, isValidNumber


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
    def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]
        self.display = display
        self.info = info
        self._equation = ""
        self._equationInitialValue = "Sua conta"
        self._left = None
        self._right = None
        self._operator = None
        self._equation = self._equationInitialValue
        self._makeGrid()

        @property
        def equation(self):
            return self._equation

        @equation.setter
        def equation(self, value):
            self._equation = value
            self.info.setText(value)

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        """
        Connects the button's clicked signal to the provided slot.
        """
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == "C":
            self._connectButtonClicked(button, self._clear)
        if text in "+-*/":
            self._connectButtonClicked(
                button, self._makeSlot(self._insertOperator, button)
            )
        if text == "=":
            self._connectButtonClicked(button, self._makeSlot(self._eq, button))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    def _insertButtonTextToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _insertOperator(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            print("Nada para colocar na esquerda")
            return
        if self._left is None:
            self._left = float(displayText)

        self._operator = buttonText
        self.equation = f"{self._left} {self._operator} ??"

    def _eq(self):
        displayText = self.display.text()
        if (
            not isValidNumber(displayText)
            or self._left is None
            or self._operator is None
        ):
            print("Nada para calcular")
            return
        self._right = float(displayText)
        self.equation = f"{self._left} {self._operator} {self._right}"
        result = eval(self.equation)
