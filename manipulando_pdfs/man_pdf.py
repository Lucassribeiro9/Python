# manipulando arquivos pdfs
# Importando as bibliotecas necessárias
from csv import writer
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Definindo o caminho do arquivo pdf
ROOT_DIR = Path(__file__).parent
PASTA_ORIGINAL = ROOT_DIR / 'pdf_originais'
PASTA_FINAL = ROOT_DIR / 'pdf_novo'
REL_BACEN = PASTA_ORIGINAL / 'pdftestebc.pdf'

reader = PdfReader(REL_BACEN)
print(len(reader.pages))
page0 = reader.pages[0]
image0 = page0.images[0]


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_FINAL / f'pdftestebc_{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

files = [PASTA_FINAL / f'pdftestebc_{i}.pdf' for i in range(len(reader.pages))]
# Criando um arquivo CSV com os dados do PDF
merger = PdfMerger()
for pdf in files:
    merger.append(pdf)
merger.write(PASTA_FINAL / 'pdftestebc_final.pdf')
merger.close()