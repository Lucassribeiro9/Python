"""Exercício
1.1 Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária.
Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?
1.2 Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?
"""

# 1.1
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    etapas = 0
    
    while baixo <= alto:
        etapas += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return etapas
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return etapas

minha_lista = [i for i in range(128)]
print(pesquisa_binaria(minha_lista, 4))

# 1.2
minha_lista = [i for i in range(256)]
print(pesquisa_binaria(minha_lista, 4))
