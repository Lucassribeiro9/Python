def add_repr(cls):
   cls.__repr__ = meu_repr
   return cls
def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
@add_repr
class Times:
    def __init__(self, nome):
        self.nome = nome
    
@add_repr   
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    

brasil = Times('Brasil')
portugal = Times('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil, portugal, terra, marte)