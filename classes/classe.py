class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = Pessoa('Lucas', 'Ribeiro')
p2 = Pessoa('Carlos', 'Silva')

print(p1.nome, p2.nome) 