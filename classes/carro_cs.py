class Carro:
    def __init__(self, nome, cor, marca, placa):
        self.nome = nome
        self.cor = cor
        self.marca = marca
        self.placa = placa
    
    def acelerar(self):
        print(f'{self.nome} Acelerando...')

nome = input('Nome: ')
cor = input('Cor: ')
marca = input('Marca: ')
placa = input('Placa: ')
carro = Carro(nome, cor, marca, placa)
carro.acelerar() 