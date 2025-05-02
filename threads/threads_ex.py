# processamentos paralelos com Python
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting {self.name}")
        sleep(self.delay)
        print(f"Exiting {self.name}")

    
def vai_demorar(texto, tempo):
        sleep(tempo)
        print(texto)

t1 = Thread(target=vai_demorar, args=("Thread 1", 2))
t1.start()
t2 = Thread(target=vai_demorar, args=("Thread 2", 4))
t2.start()

while t1.is_alive():
    print("Thread 1 ainda está viva")
    sleep(2)
print("Thread 1 já morreu")