# DOCKER PYTHON
FROM python:3.12.2-slim-bookworm

# Diretório do Container
WORKDIR /workspace

# Copiando os arquivos para o Container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos
COPY . .

