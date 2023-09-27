from itertools import groupby
alunos = [{'nome': 'João', 'nota': 'A'},
          {'nome': 'Pedro', 'nota': 'B'},
          {'nome': 'Julia', 'nota': 'A'},
          {'nome': 'Ana', 'nota': 'C'},
          {'nome': 'Lucas', 'nota': 'A'},
          {'nome': 'Maria', 'nota': 'B'}
          ]
def ordena_nota(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena_nota)
grupos = groupby(alunos_agrupados, key=ordena_nota)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)