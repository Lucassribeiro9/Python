import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtGui import QKeyEvent
from typing import cast
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.sendButton.clicked.connect(self.changeLabelResult)
    def changeLabelResult(self):
        text = self.inputName.text()
        self.labelResult.setText(f"Ce ta bem, {text}?")
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            self.inputName.setText(event.text())
        return super().eventFilter(watched, event)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()