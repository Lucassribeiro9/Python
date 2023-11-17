class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return Pessoa.ano_atual - self.idade
dados = {'nome': 'Lucas', 'idade': 26}    
p1 = Pessoa(**dados)
print(vars(p1))
print(p1.get_ano_nasc())