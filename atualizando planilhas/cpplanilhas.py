import pandas as pd
from pathlib import Path

# Definindo os caminhos para as planilhas na área de trabalho
plan1 = Path.home() / 'Desktop' / 'planilha1.xlsx'
plan2 = Path.home() / 'Desktop' / 'planilha2.xlsx'

# Verifica se ambas as planilhas existem
if plan1.exists() and plan2.exists():
    print('Ambas as planilhas existem')

try:
    # Tenta ler as planilhas
    df1 = pd.read_excel(plan1)
    df2 = pd.read_excel(plan2)
except FileNotFoundError:
    # Se uma ou ambas as planilhas não forem encontradas
    print("Uma ou ambas as planilhas não foram encontradas")
except pd.errors.EmptyDataError:
    # Se uma ou ambas as planilhas estiverem vazias
    print("Uma ou ambas as planilhas estão vazias")
except pd.errors.ParserError:
    # Se houver erro ao ler uma ou ambas as planilhas
    print("Erro ao ler uma ou ambas as planilhas")

try:
    # Define as colunas de interesse
    colunas = ['Nome', 'Idade']
    # Concatena as colunas de interesse de df1 em df2, ignora índices e remove duplicatas
    df2 = pd.concat([df2, df1[colunas]], ignore_index=True).drop_duplicates()
    # Salva o DataFrame df2 atualizado de volta na planilha2
    df2.to_excel(plan2, index=False)
except KeyError:
    # Se as colunas necessárias não forem encontradas em uma ou ambas as planilhas
    print("Uma ou ambas as planilhas não contêm as colunas necessárias")
except Exception as e:
    # Captura qualquer outro tipo de erro
    print(f"Ocorreu um erro: {e}")
finally:
    # Indica que o processo foi concluído
    print("Processo concluído")
