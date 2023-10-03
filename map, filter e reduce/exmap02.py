'''
Exercício 2: Converter uma lista de números em uma lista de strings representando esses números.
'''
def converter_para_string(lista):
    return [str(numero) for numero in lista]
    
numeros = [1, 2, 3, 4, 5]
numeros_string = list(map(str, numeros))

print(numeros)
print(numeros_string)
