import os
import pandas as pd
from pathlib import Path

# Definindo os caminhos para as planilhas na área de trabalho
plan1 = Path('P:/Publico/COMUM/CERTIFICADO DIGITAL/E-CNPJ - CERTIFICADOS ATUALIZADOS.xlsx')
plan2 = Path('C:/Users/administrador/OneDrive - DACOTA AUDICONTABIL SS/Planilhas_automate/cert_teste.xlsx')

# Verifica se ambas as planilhas existem e têm permissão de leitura
if not (os.path.exists(plan1) and os.path.exists(plan2)):
    print("Uma ou ambas as planilhas não existem")
    exit()

if not (os.access(plan1, os.R_OK) and os.access(plan2, os.R_OK)):
    print("Uma ou ambas as planilhas não podem ser lidas")
    exit()

try:
    # Tenta ler as planilhas
    df1 = pd.read_excel(plan1, engine='openpyxl')
    df2 = pd.read_excel(plan2, engine='openpyxl')

    # Define as colunas de interesse
    colunas = ['CLIENTES', 'CNPJ', 'VENCIMENTO']
    
    # Verificar as colunas de cada planilha
    if not all(coluna in df1.columns for coluna in colunas):
        print("A planilha 1 está faltando as colunas necessárias")
        print(df1.columns)
        exit()

    if not all(coluna in df2.columns for coluna in colunas):
        print("A planilha 2 está faltando as colunas necessárias")
        exit()
    # Se ambas as planilhas estiverem corretas, prosseguir com o código
    if all(coluna in df1.columns for coluna in colunas) and all(coluna in df2.columns for coluna in colunas):
        print("As planilhas estão corretas, prosseguindo com o código")
        # Selecionar apenas as colunas que estão na variável colunas
        planilha_nova = df1[colunas]
        # Concatena as colunas de interesse de df1 em df2, ignora índices e remove duplicatas
        df2 = pd.concat([df2, planilha_nova], ignore_index=True, axis=1).drop_duplicates(subset=['CLIENTES', 'CNPJ'])

        # Salva o DataFrame df2 atualizado de volta na planilha2
        df2.to_excel(plan2, index=False)
        print("As planilhas estão corretas, prosseguindo com o código")
    else:
        print("Uma ou ambas as planilhas não estão corretas")
        exit()

except FileNotFoundError:
    print("Uma ou ambas as planilhas não foram encontradas")
except pd.errors.EmptyDataError:
    print("Uma ou ambas as planilhas estão vazias")
except pd.errors.ParserError:
    print("Erro ao ler uma ou ambas as planilhas")
except KeyError:
    print("Uma ou ambas as planilhas não contêm as colunas necessárias")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    print("Processo concluído")
