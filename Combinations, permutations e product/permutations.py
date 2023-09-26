# Combinações - ordem não importa - iterável + tamanho do grupo
# Permutações - ordem importa - iterável
from itertools import combinations, permutations

def print_iterable(iterable):
    print(*list(iterable), sep='\n')
    print()
    
pessoas = ['Luiz', 'Maria', 'Joaquim', 'Ana']
camisetas = ['preta', 'amarela', 'verde', 'azul']

print_iterable(combinations(pessoas, 2))
print_iterable(permutations(pessoas, 2))
