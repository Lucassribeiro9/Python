nome = input('Digite seu nome: ')
peso = int(input('Peso: '))
altura = float(input('Altura: '))

imc = peso / altura ** 2 
print(f'Seu IMC é: {imc}' )