"""Faça um programa que utilize um dicionário para armazenar as notas de um aluno em
três disciplinas: Matemática, Português e História.
Em seguida, o programa deve calcular a média das notas e imprimir o resultado."""
import os
def mediaNotas(notas):
    media = sum(notas.values()) / len(notas)
    return media
def isAprovado(nota):
    if nota >= 5:
        return print('Aprovado')
    else:
        return print('Reprovado')
notas = {}
while True:
    qtd_materias = int(input('Digite a quantidade de materias: '))
    for i in range(qtd_materias):
        materia = input('Digite a materia: ')
        nota = float(input('Digite a nota: '))
        notas[materia] = nota    
    mediaNotas(notas)
    isAprovado(mediaNotas(notas))
    resposta = input('Deseja continuar? S/N: ')
    if resposta == 'N':
        break
    else:
        os.system('cls')
        continue


