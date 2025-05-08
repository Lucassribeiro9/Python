# Redimensionando imagens
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORGINAL = ROOT_FOLDER / "block_tatum.jpg"
IMAGE_OPT_PATH = ROOT_FOLDER / "block_tatum_opt.jpg"

image = Image.open(ORGINAL)
width, height = image.size


new_width = 400
new_height = round(height * new_width / width)
new_image = image.resize(size=(new_width, new_height))
new_image.save(IMAGE_OPT_PATH, optimize=True, quality=70)