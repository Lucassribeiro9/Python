import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print("Você não passou os argumentos")
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça algo com {argumentos[1]}')
        print(f'Faça algo com {argumentos[2]}')
    except IndexError as e:
        print(f'Faltam argumentos! Erro: {e}')