from functools import partial
from types import GeneratorType
def print_iterable(iterable):
    """
    Print each element of the given iterable on a separate line.
    
    Args:
        iterable: An iterable object.
    
    Returns:
        None
    """
    print(*list(iterable), sep='\n')
    print()


produtos = [
    {'nome': 'camiseta', 'preco': 20},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'borracha', 'preco': 2},
    {'nome': 'caderno', 'preco': 5},
    {'nome': 'caneta', 'preco': 2},
]


def aumentar_porcentagem(preco, porcentagem):
    """
    Calculates the increased value of a price by a given percentage.

    Parameters:
        preco (float): The original price.
        porcentagem (float): The percentage increase.

    Returns:
        float: The increased price.
    """
    return round(preco*porcentagem, 2)

def mudar_precos_produto(produto):
    """
    A function that takes a `produto` dictionary as input and returns a new dictionary with the same values as `produto`, except for the `'preco'` key, which is updated to be `produto['preco']` increased by 10.
    
    Parameters:
        produto (dict): A dictionary representing a product, with keys `'preco'` and other optional keys.
        
    Returns:
        dict: A new dictionary with the same values as `produto`, except for the `'preco'` key, which is updated to be `produto['preco']` increased by 10.
    """
    return{**produto, 'preco': aumentar_10(produto['preco'])}

aumentar_10 = partial(aumentar_porcentagem, 1.1)

novos_produtos = list(map(mudar_precos_produto, produtos))

print_iterable(produtos)
print_iterable(novos_produtos)