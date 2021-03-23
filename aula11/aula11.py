usuario = input('Digite seu usuario')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastrado com sucesso!')