# introdução e formatação de strings
nome = 'Lucas'
idade = 26
altura = 1.91
e_maior = idade > 18
peso = 86
imc = peso / altura ** 2
# forma prática de formatar string
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))