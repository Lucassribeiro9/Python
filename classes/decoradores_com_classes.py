def add_repr(cls):
   cls.__repr__ = meu_repr
   return cls
def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if 'Terra' in resultado:
            return f'Você está em casa!'
        return resultado    
    return interno

@add_repr
class Times:
    def __init__(self, nome):
        self.nome = nome
    
@add_repr   
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'
    

brasil = Times('Brasil')
portugal = Times('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil, portugal, terra, marte)
print(terra.falar_nome())
print(marte.falar_nome())