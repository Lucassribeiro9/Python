# Herança

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Cliente(Pessoa):
  ...
  
c1 = Cliente('Lucas', 'Ribeiro')
c1.falar_classe()