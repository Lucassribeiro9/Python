def multiplicador(multiplicador):
    """
    This function returns the inner function multiplicar, which is a closure
    function that will multiply its argument by the value of the input parameter
    multiplicador. The input parameter multiplicador is a number that will be
    used as the multiplication factor. The inner function multiplicar takes
    one parameter, numero, which is the number to be multiplied. The return
    value of the inner function is the multiplication of numero and the
    multiplication factor. The return type of the inner function is the same
    as the type of the input parameter numero.
    """
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)

print(dobro(3))
print(triplo(9))
print(quadruplo(81))
