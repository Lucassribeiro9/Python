import abc
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor):
        self.saldo -= valor
        self.detalhes(f'Saque: R${valor:.2f}')
        ...
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Deposito: R${valor:.2f}')
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')    
    