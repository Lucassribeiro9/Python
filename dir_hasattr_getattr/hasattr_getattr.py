string = 'Lucas'
metodo = 'upper'
    
if hasattr(string, metodo):
    print('Existe o metodo')
    print(getattr(string, metodo)())
else:
    print('Não existe o metodo')