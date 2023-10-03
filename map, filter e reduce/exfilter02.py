'''
Exercício 2: Filtrar os elementos de uma lista que são maiores do que 10.
'''
def maior_que_10(num):
    return num > 10

numeros = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
maiores_que_10 = list(filter(maior_que_10, numeros))

print(maiores_que_10)