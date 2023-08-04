# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy
from package_ex.calculos_mod import aumento_porcentagem
from package_ex.dados_mod import produtos 


# Gere uma cópia profunda dos produtos e aplique aumento de 10% nos preços
novos_produtos = [
    {**p, 'preco': round(aumento_porcentagem(p['preco'], 1.1), 2)}
    for p in copy.deepcopy(produtos)
]




# Ordene os produtos pelo nome em ordem decrescente
produtos_ordenados_por_nome = sorted(produtos, key=lambda p: p['nome'])
# Gere uma cópia profunda dos produtos ordenados por nome
p_ordenados_nome_copy = copy.deepcopy(produtos_ordenados_por_nome)
# Ordene os produtos pelo preço em ordem crescente
produtos_ordenados_por_preco = sorted(produtos, key=lambda p: p['preco'])
# Gere uma cópia profunda dos produtos ordenados por preço
p_ordenados_preco_copy = copy.deepcopy(produtos_ordenados_por_preco)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*p_ordenados_nome_copy, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*p_ordenados_preco_copy, sep='\n')

 