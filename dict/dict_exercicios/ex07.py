# mais um exemplo de lista com numeros aleatorios

from random import sample

def lista_random(num_lista, qtd_lista, inf_range, sup_range):
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