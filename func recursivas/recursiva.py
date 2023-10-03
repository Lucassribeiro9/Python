def recursiva(inicio = 0, fim = 10):
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)


print(recursiva()) # 10
print(fatorial(5)) # 120