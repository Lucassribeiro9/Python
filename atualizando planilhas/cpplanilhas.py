# Este script lê duas planilhas e salva as colunas desejadas em uma terceira
# planilha.

# Importa as bibliotecas necessárias
import pandas as pd
from pathlib import Path
import os

# Definindo os caminhos para as planilhas na área de trabalho
# A primeira planilha é a que vem da área de trabalho
plan1 = Path('P:/Publico/COMUM/CERTIFICADO DIGITAL/E-CNPJ - CERTIFICADOS ATUALIZADOS.xlsx')
# A segunda planilha é a que está na área de trabalho do usuário
plan2 = Path.home() / 'Desktop' / 'cert_teste.xlsx'
# A pasta atual é a pasta do Desktop
pasta_atual = Path.home() / 'Desktop'

# Verifica se ambas as planilhas existem e têm permissão de leitura
if not (plan1.exists() and plan2.exists()):
    # Se uma ou ambas as planilhas não existem, sai do script
    print("Uma ou ambas as planilhas não existem")
    exit()

if not (os.access(plan1, os.R_OK) and os.access(plan2, os.R_OK)):
    # Se uma ou ambas as planilhas não podem ser lidas, sai do script
    print("Uma ou ambas as planilhas não podem ser lidas")
    exit()

try:
    # Tenta ler as planilhas
    # A primeira planilha é lida com a engine 'openpyxl'
    df1 = pd.read_excel(plan1, engine='openpyxl', sheet_name='CERTIFICADOS EMPRESAS ATIVAS')
   
    # Salvar a planilha nova na pasta atual
    # A planilha vazia é salva com o nome 'planilha_vazia.xlsx'
    planilha_vazia = pasta_atual / 'planilha_vazia.xlsx'
    df1.to_excel(planilha_vazia, index=False)
    # A planilha vazia é lida com a engine 'openpyxl'
    df2 = pd.read_excel(planilha_vazia, engine='openpyxl')
    # Define as colunas de interesse
    colunas = ['CLIENTES', 'CNPJ', 'VENCIMENTO']
    # A variável df_select é uma seleção das colunas de interesse
    df_select = df2[colunas]
    # A planilha com as colunas de interesse é salva na planilha2
    df_select.to_excel(plan2, index=False)
    

except FileNotFoundError:
    # Se uma ou ambas as planilhas não foram encontradas, sai do script
    print("Uma ou ambas as planilhas não foram encontradas")
except pd.errors.EmptyDataError:
    # Se uma ou ambas as planilhas estão vazias, sai do script
    print("Uma ou ambas as planilhas estão vazias")
except pd.errors.ParserError:
    # Se ocorrer um erro ao ler uma ou ambas as planilhas, sai do script
    print("Erro ao ler uma ou ambas as planilhas")
except KeyError:
    # Se uma ou ambas as planilhas não contêm as colunas necessárias, sai do script
    print("Uma ou ambas as planilhas não contêm as colunas necessárias")
except Exception as e:
    # Se ocorrer um erro genérico, sai do script
    print(f"Ocorreu um erro: {e}")
finally:
    # Sai do script
    print("Processo concluído")
