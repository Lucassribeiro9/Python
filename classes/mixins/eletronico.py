from log import LogFileMixin

class Eletronico:

    def __init__(self, nome):
        self.nome = nome
        self._ligado = False # Atributo privado

    def ligar(self):
        if self._ligado:
            print(f'{self.nome} já está ligado')
            return
        print('Ligando...')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self.nome} já está desligado')
            return
        print('Desligando...')
        self._ligado = False

class Smartphone(Eletronico, LogFileMixin):

    def ligar(self):
        super().ligar()  # Chama o método da classe pai

        if self._ligado:
            msg = f'{self.nome} ligado'
            self.log_success(msg)
    def desligar(self):
        super().desligar()  # Chama o método da classe pai

        if not self._ligado:
            msg = f'{self.nome} desligado'
            self.log_error(msg)