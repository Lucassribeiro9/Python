"""
    Calculates the increased price based on a given percentage.

    Parameters:
        preco (float): The original price.
        percentual (float): The percentage increase.

    Returns:
        float: The increased price.
"""
def aumento_porcentagem(preco, percentual):
    preco = preco + (preco * percentual)
    return preco