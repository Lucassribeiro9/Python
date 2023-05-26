pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Ribeiro',
}
print(len(pessoa))
print(tuple(pessoa.keys()))
print(tuple(pessoa.values()))
print(list(pessoa.items()))
pessoa.setdefault('idade', 0)
print(pessoa['idade'])



for chave in pessoa:
    print(chave)
for valor in pessoa.values():
    print(valor)