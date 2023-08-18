# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
def zipping(x, y):
    lista_pares = list(zip(x, y))
    return lista_pares

estados = ['SP', 'RJ', 'MG', 'ES']
capitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Espírito Santo']

estados_e_capitais = zipping(estados, capitais)
print(estados_e_capitais)
