# criando dict
dict03 = {}


# ou
while True:
    entrada_key = input('Digite a chave: ')
    entrada_value = input('Digite o valor: ')
    dict03.setdefault(entrada_key, entrada_value)
    print(f'Esse é seu dicionario até aqui: {dict03}')
    print()
    continuar = input('Deseja inserir mais dados [s/n]? ')
    if continuar == 'n':
        print(f'Esse é seu dicionario: {dict03}')
        break
print('Obrigado')  