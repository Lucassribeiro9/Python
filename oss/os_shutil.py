"""
os + shutil
Mover, copiar, renomear, apagar
Mover: shutil.move
Copiar: shutil.copy
Renomear: shutil.move
Apagar: shutil.rmtree
"""

# importa as bibliotecas
import os
import shutil

# define as variaveis com os caminhos
HOME = os.path.expanduser('~') # caminho da pasta home do usuario
DESKTOP = os.path.join(HOME, 'Desktop') # caminho da pasta desktop
PASTA_ORIGINAL = os.path.join(DESKTOP, 'caju') # caminho da pasta que sera copiada
NOVA_PASTA = os.path.join(DESKTOP, 'caju2') # caminho da pasta que sera criada

#apaga toda a arvore da pasta
shutil.rmtree(NOVA_PASTA)
#copia a arvore da pasta por completo
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)