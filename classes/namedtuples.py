from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])

as_ouros = Carta('7', 'ouros')
print(as_ouros)
print(as_ouros.valor)
print(as_ouros.naipe)

for valor in as_ouros:
    print(valor)

print(as_ouros._field_defaults)
