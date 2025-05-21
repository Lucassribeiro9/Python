import sys

from main_window import MainWindow
from paths import *
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    label1 = QLabel("Texto")
    label1.setStyleSheet("font-style: 50px; font-weight: bold;")
    window.addWidgetToLayout(label1)

    icon = QIcon(str(WIN_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    window.show()

    app.exec()
