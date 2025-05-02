# processamentos paralelos com Python
from threading import Thread
from time import sleep
from threading import Lock

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print(f"Não há ingressos suficientes. Estoque atual: {self.estoque}")
            self.lock.release()
            return
        self.estoque -= quantidade
        print(f"Comprando {quantidade} ingressos. Estoque atual: {self.estoque}")
        self.lock.release()
           
           
if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(1,))
        t.start()
        sleep(2)