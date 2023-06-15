# mais um exemplo de lista com numeros aleatorios

from random import sample

def lista_random(num_lista, qtd_lista, inf_range, sup_range):
    """
    Generates a list of sorted sublists filled with random numbers within a specified range.

    :param num_lista: an integer representing the number of sublists to generate.
    :param qtd_lista: an integer representing the length of each sublist.
    :param inf_range: an integer representing the smallest number in the range of random numbers to be generated (inclusive).
    :param sup_range: an integer representing the largest number in the range of random numbers to be generated (inclusive).
    :return: a list of sorted sublists filled with random numbers within the specified range.
    """
    lista = list()
    for c in range(1, num_lista + 1):
        lista.append(sorted(sample(range(inf_range, sup_range + 1), qtd_lista)))
    return lista

num = int(input('Digite o número de listas: '))
qtd = int(input('Quantos números dentro das listas: '))
range_inf = int(input('Limite inferior do range: '))
range_sup = int(input('Limite superior do range: '))

for i in lista_random(num, qtd, range_inf, range_sup):
    print(i)