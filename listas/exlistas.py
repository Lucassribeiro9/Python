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
        item = input('Digite o nome do item: ').strip()
        lista.insert(0, item)
    if escolha == 'a':
        indice = int(input('Escolha o índice para apagar: '))
        lista.pop(indice)
    if escolha == 'l':
        indices = range(len(lista))
        for item in indices:
            print(f'{item} - {lista[item]}')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    os.system('clear')
    if resp == 'N':
        break
    