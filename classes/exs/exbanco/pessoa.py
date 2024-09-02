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

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta = None

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
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'nome={self._nome}, idade={self._idade}'
        return f'{class_name}({attrs})'
    
if __name__ == '__main__':
    import contas
    c1 = contas.ContaCorrente(123, 'Lucas', 1000)
    c2 = contas.ContaPoupanca(456, 'Carlos', 1000)
    c3 = Cliente('Maria', 30)