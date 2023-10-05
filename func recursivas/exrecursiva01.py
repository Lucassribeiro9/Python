"""
 Escreva uma função recursiva que calcule o fatorial de um número inteiro positivo. O fatorial de um número N é o produto de todos os números inteiros de 1 a N. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1, que é igual a 120.
"""

def fatorial (n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("Digite um número para o fatorial: "))
print('O fatorial de', num,'é',fatorial(num))
