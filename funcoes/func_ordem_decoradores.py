def parametros_decorador(nome):
    def decorador(func):
        print('Decorador: ', nome)

        def nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return nova_funcao
    return decorador

@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(a, b):
    return a + b

soma_cinco = soma(10, 5)
print(soma_cinco)