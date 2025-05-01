# Explicação:
# - Importamos o módulo csv para manipular arquivos CSV e Path do pathlib para manipular caminhos de arquivo.
# - Definimos uma constante ARQUIVO_CSV que representa o caminho para o arquivo CSV.
# - Criamos funções para ler e escrever arquivos CSV usando csv.reader, csv.DictReader, csv.writer, e csv.DictWriter.
# - Especificamos 'newline=""' ao abrir arquivos para evitar problemas de linhas em branco extras no Windows.
# - As funções são organizadas para que cada uma tenha uma responsabilidade clara.

# Exemplos de uso:
# - Lendo um arquivo CSV como uma lista:
#   ler_csv_como_lista()
# - Lendo um arquivo CSV como um dicionário:
#   ler_csv_como_dicionario()
# - Escrevendo em um arquivo CSV usando uma lista:
#   escrever_csv_com_lista()
# - Escrevendo em um arquivo CSV usando um dicionário:
#   escrever_csv_com_dicionario({'nome': 'João', 'idade': 25, 'sexo': 'masculino', 'altura': 1.80})
import csv
from pathlib import Path

ARQUIVO_CSV = Path(__file__).parent / 'arquivo-aula.csv'


def ler_csv_como_lista(arquivo=ARQUIVO_CSV):
    """Lê um arquivo CSV e retorna cada linha como uma lista."""
    with arquivo.open('r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        return [linha for linha in leitor]


def ler_csv_como_dicionario(arquivo=ARQUIVO_CSV):
    """Lê um arquivo CSV e retorna cada linha como um dicionário."""
    with arquivo.open('r', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)
        return [linha for linha in leitor]


def escrever_csv_com_lista(linhas, arquivo=ARQUIVO_CSV):
    """Escreve linhas em um arquivo CSV usando lista."""
    with arquivo.open('w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(linhas)
    print(f'Arquivo {arquivo} criado com sucesso.')


def escrever_csv_com_dicionario(linhas, arquivo=ARQUIVO_CSV):
    """Escreve linhas em um arquivo CSV usando dicionário."""
    with arquivo.open('w', newline='') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
        escritor.writeheader()
        escritor.writerows(linhas)
    print(f'Arquivo {arquivo} criado com sucesso.')


if __name__ == '__main__':
    print('Lendo como lista:')
    print(ler_csv_como_lista())
    print('Lendo como dicionário:')
    print(ler_csv_como_dicionario())
    print('Escrevendo como lista:')
    escrever_csv_com_lista([['nome', 'idade', 'sexo', 'altura'], ['carla', 25, 'feminino', 1.65]])
    print('Escrevendo como dicionário:')
    escrever_csv_com_dicionario([{'nome': 'João', 'idade': 25, 'sexo': 'masculino', 'altura': 1.80}])

