class Escritor:
    def __init__(self,nome):
        self._nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
       return self._ferramenta 
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
class FerramentaDeEscrita:
    def __init__(self,nome):
        self.__nome = nome
    
    def escrever(self):
        return f'{self.__nome} esta escrevendo'
    
escritor = Escritor('João')
caneta = FerramentaDeEscrita('Caneta')
maquina = FerramentaDeEscrita('Maquina')
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())
print(maquina.escrever())