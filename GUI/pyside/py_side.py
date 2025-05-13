import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

button = QPushButton("Texto")
button.setStyleSheet("font-size: 40px;")
button2 = QPushButton("Texto 2")
button2.setStyleSheet("font-size: 20px;")

central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)
layout.addWidget(button)
layout.addWidget(button2)
central_widget.show()
app.exec()
