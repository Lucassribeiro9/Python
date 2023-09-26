# Combinações - ordem não importa - iterável + tamanho do grupo
# Permutações - ordem importa - iterável
# Produto - iterável
from itertools import combinations, permutations, product

def print_iterable(iterable):
    print(*list(iterable), sep='\n')
    print()
    
pessoas = ['Luiz', 'Maria', 'Joaquim', 'Ana']
camisetas = ['preta', 'amarela', 'verde', 'azul'], ['p', 'm', 'g']

#print_iterable(combinations(pessoas, 2))
#print_iterable(permutations(pessoas, 2))
print_iterable(product(*camisetas))