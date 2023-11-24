class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    @property
    def cor(self):
        print('Lendo cor da tinta...')
        return self.cor_tinta    
        
caneta = Caneta('Azul')
print(caneta.cor)