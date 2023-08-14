#Funções decoradas

def criar_funcao(funcao):
    def funcao_decorada(*args, **kwargs):
        print('Executando a função')
        for arg in args:
            is_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f'Resultado da função: {resultado}')
        print('Finalizando a função')
        return resultado
    return funcao_decorada

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def is_string(string):
    if not isinstance(string, str):
        raise TypeError('O argumento precisa ser uma string.')


invertida = inverte_string('123')
print(invertida)