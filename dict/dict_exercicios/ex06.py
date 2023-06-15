import random

lista = [random.randint(1,60) for i in range(10)]


for i in lista:
    if i % 2 == 0:
        print(i)
print("--------------------------------")
print(lista)    

# outro exemplo que pode ser feito com listas dentro de listas

def lista_usuario(tamanho):
    """
    Generates a list of lists with the specified length, where each inner list contains 10 random integers between 1 and 50. 

    Args:
        tamanho (int): The number of inner lists to generate.

    Returns:
        list: A list of sub-lists, where each sub-list contains 10 random integers.
    """
    lst = []
    for i in range(tamanho):
        sub_lst = []
        for i in range(10):
            sub_lst.append(random.randint(1,50))
        lst.append(sub_lst)
    return lst

print(lista_usuario(8))