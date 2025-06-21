import math

from consts import MEDIUM_FONT
from main_window import MainWindow
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from style.display import Display
from style.info import Info
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
    def __init__(
        self, display: Display, info: Info, window: MainWindow, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["N", "0", ".", "="],
        ]
        self.display = display
        self.info = info
        self.window = window
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
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.operatorPressed.connect(self._configLeftOp)
        self.display.inputPressed.connect(self._insertButtonTextToDisplay)

        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button_text)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        """
        Connects the button's clicked signal to the provided slot.
        """
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        if text == "◀":
            self._connectButtonClicked(button, self._backspace)
        if text == "C":
            self._connectButtonClicked(button, self._clear)
        if text in "+-*/^":
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOp, button.text())
            )
        if text == "=":
            self._connectButtonClicked(button, self._makeSlot(self._eq))
        if text == "N":
            self._connectButtonClicked(button, self._makeSlot(self._invertNumber))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _insertButtonTextToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        if self._operator:
            self.equation = f"{self._left} {self._operator} {self.display.text()}"
        else:
            self.equation = self.display.text()

    @Slot()
    def _backspace(self):
        self.display.backspace()

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        self.display.setText(str(-float(displayText)))
        if self._operator:
            self.equation = f"{self._left} {self._operator} {self.display.text()}"
        else:
            self.equation = self.display.text()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError("Insira um número válido antes de inserir um operador")
            return
        if self._left is None:
            self._left = float(displayText)

        self._operator = text
        self.equation = f"{self._left} {self._operator} ??"

    @Slot()
    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            self._showError("Nada para calcular. Insira um número válido")
            return
        self._right = float(displayText)
        self.equation = f"{self._left} {self._operator} {self._right}"
        result = "error"

        try:
            if "^" in self.equation:
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Divisão por zero não é permitida")
            return
        except OverflowError:
            self._showError("Resultado muito grande para ser calculado")
            return

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == "error":
            self._left = None

    @Slot()
    def _showError(self, message):
        msg_box = self.window.makeMsgBox()
        msg_box.setText(message)
        msg_box.setWindowTitle("Erro")
        msg_box.setIcon(msg_box.Icon.Warning)
        msg_box.exec()
