from abc import ABC, abstractmethod

class Notificacao(ABC):
    
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...
class NotificacaoEmail(Notificacao):
    def __init__(self, mensagem):
        super().__init__(mensagem)

    def enviar(self) -> bool:
        print(f'Email enviado: {self.mensagem}')
        return True
class NotificacaoSms(Notificacao):
    def __init__(self, mensagem):
        super().__init__(mensagem)

    def enviar(self) -> bool:
        print(f'SMS enviado: {self.mensagem}')
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Falha na notificação')

notificacao_email = NotificacaoEmail('Email')
notificacao_sms = NotificacaoSms('SMS')
notificar(notificacao_email)
notificar(notificacao_sms)