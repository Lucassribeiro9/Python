import json
CAMINHO_ARQUIVO = 'c:/Users/administrador/Documents/Python repo/Python/classes/exs/dados.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
def salvar_json():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Dumping...')
        json.dump(dados, arquivo, indent=4)
            
p1 = Pessoa('Lucas', 26)
p2 = Pessoa('Carlos', 28)
p3 = Pessoa('Maria', 30)
dados = [vars(p1), vars(p2), vars(p3)]

if __name__ == '__main__':
    salvar_json()