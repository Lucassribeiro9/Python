class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor = cor
    @property
    def cor(self):
        print('Lendo cor da tinta...')
        return self.cor_tinta    
    @cor.setter
    def nova_cor(self, valor):
        print('Alterando cor da tinta...')
        self._cor = valor    
caneta = Caneta('Azul')
print(caneta.cor)
caneta.nova_cor = 'Vermelho'
print(caneta.cor) 