# trabalhando com secrets
import secrets
import string as rd
from secrets import SystemRandom as SR

# secrets é um módulo que fornece funções para geração de números aleatórios seguros
# SystemRandom é uma classe que fornece métodos para geração de números aleatórios
# que são seguros para uso em aplicações que necessitam de um alto nível de segurança
random = secrets.SystemRandom()

# string.ascii_letters retorna uma string com todas as letras do alfabeto maiúsculas e minúsculas
# string.digits retorna uma string com todos os dígitos numéricos
# string.punctuation retorna uma string com todos os caracteres de pontuação
# juntamos essas strings em uma única para ter um universo de caracteres maior
# choices seleciona k elementos aleatórios da lista de caracteres, sem repetição
# e retorna uma lista com esses elementos
# join une todos os elementos da lista em uma string única
print(''.join(SR().choices(rd.ascii_letters + rd.digits + rd.punctuation, k=8)))

