# Redimensionando imagens

# Importa as bibliotecas necessárias
from pathlib import Path

from PIL import Image

# Define o diretório raiz e os caminhos para as imagens original e otimizada
ROOT_FOLDER = Path(__file__).parent
ORGINAL = ROOT_FOLDER / "block_tatum.jpg"
IMAGE_OPT_PATH = ROOT_FOLDER / "block_tatum_opt.jpg"

# Abre a imagem original
image = Image.open(ORGINAL)

# Obtém as dimensões da imagem
width, height = image.size

# Define a nova largura e calcula a nova altura mantendo a proporção
new_width = 400
new_height = round(height * new_width / width)

# Redimensiona a imagem
new_image = image.resize(size=(new_width, new_height))

# Salva a nova imagem com otimização e qualidade ajustada
new_image.save(IMAGE_OPT_PATH, optimize=True, quality=70)
