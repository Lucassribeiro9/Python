# Combinações - ordem não importa - iterável + tamanho do grupo
from itertools import combinations

pessoas = ['Luiz', 'Maria', 'Joaquim', 'Ana']
camisetas = ['preta', 'amarela', 'verde', 'azul']

print(*list(combinations(pessoas, 2)), sep='\n')