import sys

from consts import WIN_ICON_PATH
from style.display import Display
from main_window import Info, MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from style.buttons import Button, ButtonGrid
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
    window.addWidgetToVLayout(label)
    # Display
    display = Display()
    window.addWidgetToVLayout(display)    # trunk-ignore(git-diff-check/error)

    # Grid
    buttonsGrid = ButtonGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Button
    buttonsGrid.addWidget(Button(0), 0, 0)
    buttonsGrid.addWidget(Button(1), 0, 1)
    buttonsGrid.addWidget(Button(2), 0, 2)

    window.adjustFixedSize()
    window.show()
    app.exec()
