import random

lista = [random.randint(1,60) for i in range(10)]


for i in lista:
    if i % 2 == 0:
        print(i)
print("--------------------------------")
print(lista)    

# outro exemplo que pode ser feito com listas dentro de listas

def lista_usuario(tamanho):
    lst = []
    for i in range(tamanho):
        sub_lst = []
        for i in range(10):
            sub_lst.append(random.randint(1,50))
        lst.append(sub_lst)
    return lst

print(lista_usuario(8))