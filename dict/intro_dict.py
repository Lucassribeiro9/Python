pessoa = {}

chave = 'nome'
pessoa[chave] = 'Lucas'
print(pessoa[chave])

chave2 = 'sobrenome'
pessoa[chave2] = 'Ribeiro'

del pessoa['sobrenome']
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa.get('sobrenome'))

