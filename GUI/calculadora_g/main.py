import sys

from consts import WIN_ICON_PATH
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style.buttons import ButtonGrid
from style.display import Display
from style.info import Info
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
    info = Info("Sua conta")
    window.addWidgetToVLayout(info)
    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
