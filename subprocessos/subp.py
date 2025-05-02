import subprocess
import sys

# Define o comando padrão para executar um ping no localhost
cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf-8'  # Define a codificação padrão como UTF-8
system = sys.platform  # Obtém o sistema operacional atual

# Verifica o sistema operacional e ajusta o comando e a codificação
if system == 'win32':  # Caso seja Windows
    cmd = ["cmd", "/c", "dir"]  # Executa o comando 'dir' no shell do Windows
    encoding = 'cp850'  # Define a codificação padrão do Windows
elif system == 'linux':  # Caso seja Linux
    cmd = ["ls", "-l"]  # Executa o comando 'ls -l' no Linux
    encoding = 'utf-8'  # Define a codificação como UTF-8
elif system == 'darwin':  # Caso seja macOS
    cmd = ["ls", "-l"]  # Executa o comando 'ls -l' no macOS
    encoding = 'utf-8'  # Define a codificação como UTF-8

print(system)  # Imprime o sistema operacional detectado

# Executa o comando definido usando subprocess.run
proc = subprocess.run(cmd, capture_output=True, text=True, encoding=encoding)

# Imprime a saída do comando executado
print(proc.stdout)
