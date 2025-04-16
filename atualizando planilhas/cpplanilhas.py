# Este script lê duas planilhas e salva as colunas desejadas em uma terceira
# planilha.

# Importa as bibliotecas necessárias
import pandas as pd
from pathlib import Path
import os

def executar_atualizacao():
    # Código que você deseja testar
    plan1 = Path('P:/Publico/COMUM/CERTIFICADO DIGITAL/E-CNPJ - CERTIFICADOS ATUALIZADOS.xlsx')
    plan2 = Path('C:/Users/administrador/OneDrive - DACOTA AUDICONTABIL SS/Planilhas_automate/cert_teste.xlsx')
    pasta_atual = Path.home() / 'Desktop'

    # Verifica se ambas as planilhas existem e têm permissão de leitura
    if not (plan1.exists() and plan2.exists()):
        print("Uma ou ambas as planilhas não existem")
        return False

    if not (os.access(plan1, os.R_OK) and os.access(plan2, os.R_OK)):
        print("Uma ou ambas as planilhas não podem ser lidas")
        return False

    try:
        # Tenta ler as planilhas
        df1 = pd.read_excel(plan1, engine='openpyxl', sheet_name='CERTIFICADOS EMPRESAS ATIVAS')
        planilha_vazia = pasta_atual / 'planilha_vazia.xlsx'
        df1.to_excel(planilha_vazia, index=False)
        df2 = pd.read_excel(planilha_vazia, engine='openpyxl')
        colunas = ['CLIENTES', 'CNPJ', 'VENCIMENTO']
        df_select = df2[colunas]
        with pd.ExcelWriter(plan2, mode='a', if_sheet_exists='replace') as writer:
            df_select.to_excel(writer, sheet_name='Planilha2', startrow=1, header=False, index=False)
        print("Planilha atualizada com sucesso!")
        return True, df_select
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("Processo concluído")
