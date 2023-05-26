p1 = {
    'nome': 'Lucas',
    'sobrenome': 'Ribeiro',
}
print(p1.get('nome', 'Não existe'))
# nome = p1.pop('nome')
nome = p1.popitem()
print(nome)
print(p1)
""" p1.update({
    'idade': 25,
})
"""
p1.update(nome='Carlos', idade=28)
print(p1)
tupla = ('casa', 'apartamento'), ('número', 2)
p1.update(tupla)
print(p1)
