from collections import deque

fila_correta: deque[int] = deque()
fila_correta.append(1)
fila_correta.append(2)
fila_correta.append(3)
fila_correta.appendleft(0)
print(fila_correta)
fila_correta.pop()
print(fila_correta)