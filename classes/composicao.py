class Cliente:
    def __init__(self, nome, ):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))
    
    def listar_enderecos(self):
        for end in self.enderecos:
            print(end.rua, end.numero)
    
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print(f'{self.rua}, {self.numero} foi apagado')
        
cliente1 = Cliente('João')
cliente1.inserir_endereco('Av. Brasil', 100)
cliente2 = Cliente('Maria')
cliente2.inserir_endereco('Av. Parana', 200)
cliente1.listar_enderecos()

del cliente1
print('---- Fim de código ----')