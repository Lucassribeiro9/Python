from functools import reduce
'''
Exercício 1: Calcular a soma de todos os elementos de uma lista.
'''

def soma(a, b):
    return a+b

numeros = [1, 2, 3, 4, 5]
somatoria = reduce(soma, numeros)
print(somatoria)


