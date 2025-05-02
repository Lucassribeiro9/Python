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

t1 = MyThread("Thread-1", 5)
t1.start()
t2 = MyThread("Thread-2", 3)
t2.start()
t3 = MyThread("Thread-3", 1)
t3.start()

for i in range(20):
    print(i)
    sleep(1)