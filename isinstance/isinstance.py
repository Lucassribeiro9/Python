lista = [
    'a', 1, 1.1, True, [0,1,2,3], {0, 1}, {'nome': 'Lucas'}
]
for item in lista:
    if isinstance(item, set):
        item.add(3)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('String: ', item.upper())
    elif isinstance(item, (int, float)):
        print('Number')
        print(item, item * 5)
    else:
        print('Outros')
        print(item)