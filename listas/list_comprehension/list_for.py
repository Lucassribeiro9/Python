lista = []
for x in range(5):
    for y in range(5):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
lista_comp = [
    [(n, letra) for letra in 'Lucas']
    for n in range(5)
]
print(lista)
print(lista_comp)