# Abstração
# Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
   
    def log_error(self, msg):
        return self.log(f'ERRO: {msg}')
    
    def log_success(self, msg):
        return self.log(f'SUCESSO: {msg}')

class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no log: ', msg_formatada)
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatada + '\n')
class LogPrintMixin(Log):
    def log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')        

if __name__ == '__main__':
   lp = LogPrintMixin()
   lf = LogFileMixin()
   lp.log_error('Algum erro')
   lp.log_success('Algum sucesso')
   lf.log_error('Algum erro')
   lf.log_success('Algum sucesso')