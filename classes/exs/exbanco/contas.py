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
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'agencia={self.agencia}, conta={self.conta}, saldo={self.saldo}'
        return f'{class_name}({attrs})'
class ContaPoupanca(Conta):
        def sacar(self, valor):
            valor_pos_saque = self.saldo - valor
            if valor_pos_saque > 0:
                self.saldo -= valor
                self.detalhes(f'Saque: R${valor:.2f}')
                return self.saldo
        
            print('Saldo insuficiente para saque')
            self.detalhes(f'Saldo insuficiente para saque: R${valor:.2f}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo + self.limite - valor
        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detalhes(f'Saque: R${valor:.2f}')
            return self.saldo

        print('Saldo insuficiente para saque')
        self.detalhes(f'Saldo insuficiente para saque: R${valor:.2f}')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'agencia={self.agencia}, conta={self.conta}, saldo={self.saldo}, limite={self.limite}'
        return f'{class_name}({attrs})'
if __name__ == '__main__':
    ...