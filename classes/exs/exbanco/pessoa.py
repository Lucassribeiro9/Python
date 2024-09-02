class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade