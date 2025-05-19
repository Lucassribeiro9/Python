# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

# criar aplicação
app = QApplication(sys.argv)
# criar janela principal
window = QMainWindow()
# criar widget central
central_widget = QWidget()
# definir o widget central na janela principal
window.setCentralWidget(central_widget)
# definir o título da janela
window.setWindowTitle("Minha janela bonita")

# criar botões
botao1 = QPushButton("Texto do botão")
botao1.setStyleSheet("font-size: 80px;")
botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 40px;")
botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 40px;")

# criar layout
layout = QGridLayout()
# definir o layout no widget central
central_widget.setLayout(layout)

# adicionar botões ao layout
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    # mostrar mensagem na barra de status
    status_bar.showMessage("O meu slot foi executado")


# status bar
status_bar = window.statusBar()
# mostrar mensagem na barra de status
status_bar.showMessage("Mostrar mensagem na barra")

# menu bar
menu = window.menuBar()
# criar menu
primeiro_menu = menu.addMenu("Primeiro menu")
# criar ação no menu
primeira_acao = primeiro_menu.addAction("Primeira ação")
# conectar ação ao slot
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)


# mostrar a janela
window.show()
# executar o loop da aplicação
app.exec()  # O loop da aplicação
