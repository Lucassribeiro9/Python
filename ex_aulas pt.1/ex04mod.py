# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
from copy import deepcopy
# from package_ex.calculos_mod import aumento_porcentagem

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Gere uma cópia profunda dos produtos e aplique aumento de 10% nos preços
novos_produtos = deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] = round(produto['preco']* 1.1)

# Ordene os produtos pelo nome em ordem decrescente
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda produto: produto['nome'], reverse=True)

# Gere uma cópia profunda dos produtos ordenados por nome
produtos_ordenados_por_nome = deepcopy(produtos_ordenados_por_nome)

# Ordene os produtos pelo preço em ordem crescente
produtos_ordenados_por_preco = sorted(novos_produtos, key=lambda produto: produto['preco'])

# Gere uma cópia profunda dos produtos ordenados por preço
produtos_ordenados_por_preco = deepcopy(produtos_ordenados_por_preco)

print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')

 