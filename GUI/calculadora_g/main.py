import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    label1 = QLabel("Texto")
    label1.setStyleSheet("font-style: 50px; font-weight: bold;")
    window.v_layout.addWidget(label1)
    window.adjust_FixedSize()
    window.show()

    app.exec()
