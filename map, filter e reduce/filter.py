def print_iterable(iterable):
    
    print(*list(iterable), sep='\n')
    print()

def filtrar_preco(produto):
    return produto['preco'] > 10

produtos = [
    {'nome': 'camiseta', 'preco': 20},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'borracha', 'preco': 2},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'caneta', 'preco': 2},
]

novos_produtos = filter(filtrar_preco, produtos)

print_iterable(produtos)
print_iterable(novos_produtos)