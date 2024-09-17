import os

caminho = os.getcwd()
listar = os.listdir(caminho)
acessar = os.walk(caminho)
for item in listar:
    print(item)

print(acessar)