# manipulando arquivos pdfs
# Importando as bibliotecas necessárias
from csv import writer  # Biblioteca para manipulação de arquivos CSV (não utilizada no código atual)
from pathlib import Path  # Biblioteca para manipulação de caminhos de arquivos e diretórios
from PyPDF2 import PdfReader, PdfWriter, PdfMerger  # Classes para leitura, escrita e fusão de PDFs

# Definindo o caminho do arquivo pdf
ROOT_DIR = Path(__file__).parent  # Diretório raiz do script atual
PASTA_ORIGINAL = ROOT_DIR / 'pdf_originais'  # Caminho para a pasta de PDFs originais
PASTA_FINAL = ROOT_DIR / 'pdf_novo'  # Caminho para a pasta onde os PDFs processados serão salvos
REL_BACEN = PASTA_ORIGINAL / 'pdftestebc.pdf'  # Caminho do arquivo PDF a ser manipulado

# Lendo o arquivo PDF
reader = PdfReader(REL_BACEN)  # Inicializa o leitor para o arquivo PDF especificado
print(len(reader.pages))  # Imprime o número de páginas do PDF
page0 = reader.pages[0]  # Obtém a primeira página do PDF
image0 = page0.images[0]  # Obtém a primeira imagem da primeira página (não utilizada no código)

# Iterando sobre as páginas do PDF
for i, page in enumerate(reader.pages):
    writer = PdfWriter()  # Inicializa o escritor de PDF
    with open(PASTA_FINAL / f'pdftestebc_{i}.pdf', 'wb') as arquivo:  # Cria um arquivo para cada página
        writer.add_page(page)  # Adiciona a página atual ao escritor
        writer.write(arquivo)  # Escreve a página no arquivo

# Lista de arquivos PDF gerados (um para cada página)
files = [PASTA_FINAL / f'pdftestebc_{i}.pdf' for i in range(len(reader.pages))]

# Criando um arquivo PDF final que combina todas as páginas
merger = PdfMerger()  # Inicializa o objeto para fusão de PDFs
for pdf in files:  # Itera sobre os arquivos PDF gerados
    merger.append(pdf)  # Adiciona cada arquivo ao objeto de fusão
merger.write(PASTA_FINAL / 'pdftestebc_final.pdf')  # Escreve o PDF combinado em um novo arquivo
merger.close()  # Fecha o objeto de fusão