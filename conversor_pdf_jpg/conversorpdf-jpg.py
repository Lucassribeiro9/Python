from pdf2image import convert_from_path
import os

def pdf_to_jpg(pdf_path, output_folder):
    # Converte cada página do PDF para JPG
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        # Salva cada página como um arquivo JPG
        output_file = os.path.join(output_folder, f"page_{i + 1}.jpg")
        image.save(output_file, "JPEG")
        print(f"Página {i + 1} salva em: {output_file}")

# Exemplo de uso
pdf_path = input("Digite o caminho do arquivo PDF: ")
output_folder = "output"  # Pasta de saída

# Cria a pasta de saída, se não existir
os.makedirs(output_folder, exist_ok=True)

pdf_to_jpg(pdf_path, output_folder)
