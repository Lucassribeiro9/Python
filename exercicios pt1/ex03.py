"""Faça um programa que utilize um dicionário para armazenar as notas de um aluno em
n disciplinas.
Em seguida, o programa deve calcular a média das notas e imprimir o resultado."""
import os


def mediaNotas(notas):
    media = sum(notas.values()) / len(notas)
    return media


def isAprovado(nota):
    if nota >= 5:
        return print("Aprovado")
    else:
        return print("Reprovado")


notas = {}

while True:
    while True:
        try:
            qtd_materias = int(input("Digite a quantidade de materias: "))
            if qtd_materias <= 0:
                print("A quantidade de materias deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Valor inválido")
    for i in range(qtd_materias):
        while True:
            materia = input("Digite a materia: ")
            if materia.isalpha():
                break
            else:
                print("Materia inválida.")

        while True:
            try:
                nota = float(input("Digite a nota: "))
                break
            except ValueError:
                print("Valor inválido")
        notas[materia] = nota
    mediaNotas(notas)
    print(f"Média das notas: {mediaNotas(notas):.2f}")
    isAprovado(mediaNotas(notas))
    resposta = input("Deseja continuar? S/N: ").upper()
    if resposta == "N":
        print("Programa encerrado.")
        break
    else:
        os.system("cls")
        notas = {}
        continue
