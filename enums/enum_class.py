import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()

#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO'])
def mover (direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção inválida')
    print(f'Movendo para {direcao.name} ({direcao.value})')
    
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)