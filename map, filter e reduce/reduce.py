from functools import reduce

produtos = [
    {'nome': 'camiseta', 'preco': 20},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'borracha', 'preco': 2},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'caneta', 'preco': 2},
]
def func_reduce(acumulador, produto):
    return acumulador + produto['preco']

total = reduce(func_reduce, produtos, 0)

print('O total é:',total)
