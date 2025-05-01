import os
from itertools import count

caminho = os.path.join('C:\\Users\\administrador\\Documents')
counter = count()

for diretorio, subpastas, arquivos in os.walk(caminho):
    the_count = next(counter)
    print(f'{the_count} - Diretorio: {diretorio}')
    
    for dir_name in subpastas:
        print(f'\tSubpasta: {dir_name}')
    
    for file_name in arquivos:
        print(f'\tArquivo: {file_name}')