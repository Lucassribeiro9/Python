frase = 'Frase teste de, split'
lista_frase_limpa = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_limpa):
    lista_frase.append(lista_frase_limpa[i].strip())    
print(lista_frase_limpa)
print(lista_frase)