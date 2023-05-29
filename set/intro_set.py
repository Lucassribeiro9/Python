s1 = set('Luiz')
print(s1)

s2 = s2 = {1,2,3}
#São iteráveis (for, in, not in)
print(3 in s2)
for numero in s1:
    print(numero)

# Métodos uteis
s3 = set()
s3.add('Luiz')
s3.add(1)
s3.update(('Olá', 1, 2,))
s3.discard('Luiz')
print(s3)
s3.clear()