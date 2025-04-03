# Trabalhando com o módulo random
import random
import time

# Gera um número aleatório dentro de um intervalo, excluindo o valor final
r_range = random.randrange(1, 100)  

# Gera um número inteiro aleatório entre os valores especificados, inclusive
r_int = random.randint(1, 100)  

# Gera um número de ponto flutuante aleatório entre os valores especificados
r_float = random.uniform(1, 100)  

nomes = ['Luiz', 'Otavio', 'Maria', 'Joaquim']

# Embaralha a lista 'nomes' in-place, modificando sua ordem
random.shuffle(nomes)

# Retorna uma nova lista contendo 2 elementos aleatórios da lista 'nomes'
novos_nomes = random.sample(nomes, 2)

# Escolhe um elemento aleatório da lista 'nomes'
r_choice = random.choice(nomes)

# Retorna uma lista com 2 elementos escolhidos aleatoriamente da lista 'nomes', com reposição
r_choices = random.choices(nomes, k=2)

# Define uma semente para o gerador de números aleatórios, garantindo a reprodutibilidade
random.seed(time.time())

print(f'Range: {r_range}')
print(f'Inteiro: {r_int}')
print(f'Float: {r_float}')
print(f'Embaralhado: {nomes}')
print(f'Novos nomes: {novos_nomes}')
print(f'Escolha: {r_choice}')
print(f'Escolhas: {r_choices}')

