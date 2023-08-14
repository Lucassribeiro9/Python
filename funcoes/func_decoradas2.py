def multiplos_decoradores(a=None, b=None, c=None):
    def multiplas_funcoes(funcao):
      print('Decorada 1')
      
      def aninhada(*args, **kwargs):
        print('Parametros do decorador: ', a, b, c)
        print('Aninhada')
        res = funcao(*args, **kwargs)
        return res 
      return aninhada
    return multiplas_funcoes

@multiplos_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = multiplos_decoradores()
multiplica = decoradora(lambda x, y: x * y)

soma_cinco = soma(5, 5)
mult_cinco = multiplica(5, 5)
print(soma_cinco)
print(mult_cinco)