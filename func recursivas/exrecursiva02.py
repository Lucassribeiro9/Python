"""
Exercício 2: Escreva uma função recursiva que calcule o N-ésimo termo da sequência de Fibonacci. A sequência de Fibonacci é uma sequência em que cada termo é a soma dos dois termos anteriores. Os primeiros dois termos são 0 e 1. Por exemplo, os primeiros 10 termos da sequência de Fibonacci são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
