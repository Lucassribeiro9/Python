'''
Exercício 2: Concatenar todos os elementos de uma lista de strings em uma única string.
'''
from functools import reduce

def concatenar(string, elemento):
    return string + elemento

elementos = ['a', 'b', 'c']
elementos_concatenados = reduce(concatenar, elementos)

print(elementos_concatenados)