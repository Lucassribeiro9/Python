"""
Este código utiliza o módulo pathlib para criar e manipular arquivos e diretórios.
Ele cria um diretório chamado 'Pasta da aula pathlib' na área de trabalho do usuário,
e dentro dele, um arquivo chamado 'aula240.txt'. Ele escreve o texto 'Teste' e
'Teste 2' nele, e então lê e imprime o conteúdo do arquivo.
Depois, ele cria um diretório chamado 'files' dentro do diretório anterior,
e dentro dele, cria 10 arquivos chamados 'file0.txt', 'file1.txt', ... 'file9.txt'.
Ele escreve o texto 'Teste {i}' e 'Teste 2 {i}' neles, e então lê e imprime o conteúdo
de cada arquivo.
Por fim, ele remove todos os arquivos e diretórios criados.
"""

from pathlib import Path

# Cria um objeto Path que representa o diretório atual do projeto
caminho_projeto = Path.home() / 'Desktop' / 'Pasta da aula pathlib'
# Cria o diretório se ele não existir
caminho_projeto.mkdir(parents=True, exist_ok=True)

# Cria um arquivo chamado 'aula240.txt' no diretório criado acima
arquivo = caminho_projeto / 'aula240.txt'
# Escreve o texto 'Teste' e 'Teste 2' no arquivo
with arquivo.open('w') as file:
    file.write('Teste\n')
    file.write('Teste 2\n')

# Lê e imprime o conteúdo do arquivo
print(arquivo.read_text())

# Cria um diretório chamado 'files' dentro do diretório criado acima
files = caminho_projeto / 'files'
files.mkdir(exist_ok=True)

# Cria 10 arquivos chamados 'file0.txt', 'file1.txt', ... 'file9.txt' no diretório 'files'
for i in range(10):
    file = files / f'file{i}.txt'
    # Escreve o texto 'Teste {i}' e 'Teste 2 {i}' neles
    with file.open('w') as text_file:
        text_file.write(f'Teste {i}\n')
        text_file.write(f'Teste 2 {i}\n')

# Remove todos os arquivos e diretórios criados
def rmtree(root, remove_root=True):
    for file in root.rglob('*'):
        if file.is_dir():
            print('DIR', file)
            file.rmdir()
        else:
            print('FILE', file)
            file.unlink()
    if remove_root:
        root.rmdir()

rmtree(caminho_projeto)
