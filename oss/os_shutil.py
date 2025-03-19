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

# cria a pasta caso nao exista
os.makedirs(NOVA_PASTA, exist_ok=True)

# percorre a pasta original e seus subdiretorios
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for file in files: # percorre cada arquivo
        caminho_arquivo = os.path.join(root, file) # monta o caminho do arquivo
        shutil.copy(caminho_arquivo, NOVA_PASTA) # copia o arquivo para a pasta nova
        print(f'Arquivo copiado: {caminho_arquivo}') # imprime o caminho do arquivo copiado
