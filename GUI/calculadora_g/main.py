import sys

from consts import WIN_ICON_PATH
from style.display import Display
from main_window import Info, MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style.buttons import Button
from style.styles import setupTheme

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Icon
    icon = QIcon(str(WIN_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Label
    label = Info("2.0 ^ 2.0 = 4")
    window.addToVLayout(label)
    # Display
    display = Display()
    window.addToVLayout(display)
    
    # Button
    button = Button("Text button")
    window.addToVLayout(button)

    window.adjustFixedSize()
    window.show()
    app.exec()
