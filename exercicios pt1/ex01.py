num1 = input('Digite um número inteiro: ')

if num1.isdigit():
    num1 = int(num1)
else:    
    print('Digite um número válido.')

if num1 % 2 == 0:
    print(f'O número é par: {num1}')
else:
    print(f'O número é ímpar: {num1}')
