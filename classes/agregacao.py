# Agregação

class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def total(self):
        return sum([p.preco for p in self.produtos])
    
    def inserir_produto(self, *produtos):
        for produto in produtos:
            self.produtos.append(produto)
    
    def lista_produtos(self):
        for p in self.produtos:
            print(p.nome, p.preco)
        print(f'Total: {self.total()}')
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco        
carrinho = Carrinho()
p1, p2 = Produto('Camisa', 50), Produto('Cueca', 20)
carrinho.inserir_produto(p1, p2)
carrinho.lista_produtos()
