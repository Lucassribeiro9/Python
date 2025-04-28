# Importa o módulo ArgumentParser do pacote argparse para manipulação de argumentos de linha de comando
from argparse import ArgumentParser

# Cria um objeto ArgumentParser
parser = ArgumentParser(description='Processa argumentos de linha de comando.')

# Adiciona um argumento opcional '-b' ou '--basic' que aceita múltiplas strings
parser.add_argument(
    '-b', '--basic',
    help='Mostra "Hello world" na tela',
    type=str,
    metavar='STRING',
    default='padrão',
    required=True,
    nargs='+'
)

# Analisa os argumentos da linha de comando
args = parser.parse_args()

# Verifica se algum argumento foi passado para '--basic'
if args.basic:
    print('Valor de basic:', ' '.join(args.basic))
else:
    print('Você não passou o valor de b')
