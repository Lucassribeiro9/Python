from dataclasses import dataclass, field
from typing import List

@dataclass
class Produto:
    nome: str
    preco: float
    quantidade: int = 0

@dataclass
class CarrinhoDeCompras:
    itens: List[Produto] = field(default_factory=list)

    def adicionar_item(self, produto: Produto):
        self.itens.append(produto)

    def calcular_total(self):
        return sum(item.preco * item.quantidade for item in self.itens)

# Exemplo de uso
if __name__ == "__main__":
    # Criando alguns produtos
    banana = Produto("Banana", 3.50, 5)
    maca = Produto("Maçã", 2.75, 3)
    laranja = Produto("Laranja", 4.00, 2)

    # Criando um carrinho de compras
    carrinho = CarrinhoDeCompras()

    # Adicionando produtos ao carrinho
    carrinho.adicionar_item(banana)
    carrinho.adicionar_item(maca)
    carrinho.adicionar_item(laranja)

    # Calculando o total
    total = carrinho.calcular_total()

    print(f"Total do carrinho: R$ {total:.2f}")

    # Exibindo informações dos produtos no carrinho
    for item in carrinho.itens:
        print(f"{item.nome}: R$ {item.preco:.2f} x {item.quantidade}")
