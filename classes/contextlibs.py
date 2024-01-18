from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo,modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo,modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula242.txt', 'w') as arquivo:
    arquivo.write('Teste!')
    print('WITH', arquivo)