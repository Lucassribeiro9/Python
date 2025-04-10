import pandas as pd
from pathlib import Path

plan1 = Path.home() / 'Desktop' / 'planilha1.xlsx'
plan2 = Path.home() / 'Desktop' / 'planilha2.xlsx'

if plan1.exists() and plan2.exists():
    print('Ambas as planilhas existem')

df1 = pd.read_excel(plan1)
df2 = pd.read_excel(plan2)

colunas = ['Nome', 'Idade']
df2 = pd.concat([df2, df1[colunas]], ignore_index=True).drop_duplicates()

df2.to_excel(plan2, index=False)