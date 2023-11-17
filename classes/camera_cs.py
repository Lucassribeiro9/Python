class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja esta Filmando')
            return
        print(f'{self.nome} esta Filmando')
        self.filmando = True
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar enquanto esta filmando')
            return
        print(f'{self.nome} esta fotografando')
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} nao esta Filmando')
            return
        print(f'{self.nome} parou de Filmar')
        self.filmando = False
    
        
c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.filmar()
c2.parar_filmar()
c2.fotografar()