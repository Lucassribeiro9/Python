def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)

print(dobro(3))
print(triplo(9))
print(quadruplo(81))
