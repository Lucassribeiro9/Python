"""
Faça um programa que utilize um dicionário para armazenar o nome
e a idade de três pessoas.
Em seguida, o programa deve imprimir o nome da pessoa mais velha.
"""

pessoa = [
    {'nome': 'João',
    'idade': 20,},
    {
        'nome': 'Maria',
        'idade': 18,
    },
    {
        'nome': 'Lucas',
        'idade': 28,
    },
    {
        'nome': 'Beatriz',
        'idade': 26,
    },
]
mais_velho = max(pessoa, key=lambda pessoa: pessoa['idade'])
print(mais_velho['nome'])