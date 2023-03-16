"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    escolha = input('Selecione uma opção: \n[i]nserir [a]pagar [l]istar: ').strip()
    if escolha == 'i':
        os.system('clear')
        item = input('Digite o nome do item: ').strip()
        lista.append(item)
    elif escolha == 'a':
        indice = input('Escolha o índice para apagar: ')
        try:
            int_indice = int(indice)
            del lista[int_indice]
        except IndexError:
            print('O índice informado não existe.')
        except ValueError:
            print('Por favor, digite um número de índice válido.')
        except Exception:
            print('Ocorreu um erro inesperado.')
    elif escolha == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('Não existe índice para listar')
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
    else:
        resp = str(input('Opção inválida. Quer continuar no sistema? [S/N] ')).strip().upper()[0]
        os.system('clear')
        if resp == 'N':
            print('Obrigado!.')
            break
