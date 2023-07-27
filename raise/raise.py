def nao_aceita_zero(d):
    if d == 0:
       raise ZeroDivisionError('Não é possível dividir por zero')
    return True
def erro_tipo(d):
    if not isinstance(d, int):
        raise TypeError('O número deve ser inteiro')
    return True
def divide(n, d):
    nao_aceita_zero(d)
    erro_tipo(n)
    erro_tipo(d)
    return n / d

print(divide(8, 0))
