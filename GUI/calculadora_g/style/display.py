from consts import BIG_FONT, MINIMUM_WIDTH, SMALL_FONT, TEXT_MARGIN
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {BIG_FONT}px;")
        self.setMinimumHeight(BIG_FONT * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])


class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {SMALL_FONT}px;")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
