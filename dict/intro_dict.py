pessoa = {
 'nome': 'Lucas',
 'sobrenome': 'Ribeiro',
 'idade': 28,
 'altura': 1.9,
 'endereços': [
	 {'rua': 'tal tal', 'número': 123},
	 {'rua': 'outra rua', 'número': 321},
 ] # lista com dict
}
print(pessoa)
print()
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])