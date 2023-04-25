frase = 'Frase teste de, split'
lista_frase = frase.split(',')

for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip())

print(lista_frase)