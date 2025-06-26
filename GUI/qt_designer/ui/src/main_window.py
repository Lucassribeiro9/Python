import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.sendButton.clicked.connect(self.changeLabelResult)
    def changeLabelResult(self):
        text = self.inputName.text()
        self.labelResult.setText(f"Ce ta bem, {text}?")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()