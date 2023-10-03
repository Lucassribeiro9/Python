'''
Exercício 1: Multiplicar todos os números de uma lista por 2.
'''
def dobrar(numero):
    return numero * 2

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = list(map(dobrar, numeros))

print(numeros)
print(numeros_dobrados)
