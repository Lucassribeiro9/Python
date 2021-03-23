"""
Condições IF, ELIF e ELSE - Lógicos
and, or, not
in e not in
"""
a = 2
b = 3
# and (verdadeiro e verdadeiro) = verdadeiro
if a == b and b < a:
    print('Certo')
else:
    print('Errado')
# or (verdadeiro ou verdadeiro)
if a == b or b > a:
    print('Certo')
else:
    print('Errado')
# not: contrário da expressão e geralmente é usado com variaveis vazias
# in ou not in: retornam o booleano conforme tenha ou não um item da condição
nome = 'Lucas'
if 'W' not in nome:
    print("Existe")
else:
    print('Não existe')