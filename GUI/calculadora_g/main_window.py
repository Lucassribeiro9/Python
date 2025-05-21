from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from consts import SMALL_FONT

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle("Calculadora")

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget):
        self.v_layout.addWidget(widget)

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)