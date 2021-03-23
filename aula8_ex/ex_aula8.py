nome = 'Lucas'
idade = 26
altura = 1.91
ano_atual = 2021
peso = 86
imc = peso / altura ** 2
datanasc = ano_atual - idade
# forma prática de formatar string
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Altura: {altura}')
print(f'Peso: {peso}')
print(f'Imc: {imc:.2f}')
print(f'Ano de nascimento: {datanasc}')
