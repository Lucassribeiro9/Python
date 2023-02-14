# exercicio formatação de strings

nome = input('Nome: ')
idade = input('Idade: ')

if nome and idade :
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrário: {nome[::-1]}')
    print(f'Quantidade de caracteres:{len(nome)}')
    print(f'A primeira letra do seu nome: {nome[0]}')
    print(f'A última letra: {nome[-1]}')
    if '' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
else:
    print('Campos vazios!')
    