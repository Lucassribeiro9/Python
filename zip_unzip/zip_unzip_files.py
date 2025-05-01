# zip files - compactando e descompatando arquivos
import os
import zipfile

def compactar_arquivos(caminho_pasta, nome_zip):
    """
    Compacta todos os arquivos de uma pasta em um arquivo zip
    
    Args:
        caminho_pasta (str): Caminho da pasta com arquivos para compactar
        nome_zip (str): Nome do arquivo zip a ser criado
    """
    with zipfile.ZipFile(nome_zip, 'w') as zip_file:
        for pasta_raiz, subpastas, arquivos in os.walk(caminho_pasta):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                zip_file.write(caminho_arquivo, os.path.relpath(caminho_arquivo, caminho_pasta))

def descompactar_arquivos(arquivo_zip, pasta_destino):
    """
    Descompacta um arquivo zip para uma pasta de destino
    
    Args:
        arquivo_zip (str): Caminho do arquivo zip
        pasta_destino (str): Pasta onde os arquivos serão extraídos
    """
    with zipfile.ZipFile(arquivo_zip, 'r') as zip_file:
        zip_file.extractall(pasta_destino)

# Exemplo de uso
if __name__ == "__main__":
    # Compactando arquivos
    pasta_origem = "pasta_com_arquivos"
    arquivo_zip = "arquivos_compactados.zip"
    compactar_arquivos(pasta_origem, arquivo_zip)
    
    # Descompactando arquivos
    pasta_destino = "pasta_destino"
    descompactar_arquivos(arquivo_zip, pasta_destino)
