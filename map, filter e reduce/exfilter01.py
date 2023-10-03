'''
Exercício 1: Filtrar os números pares de uma lista.
'''

def e_par(num):
    return num % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(e_par, numeros))

print(numeros_pares)