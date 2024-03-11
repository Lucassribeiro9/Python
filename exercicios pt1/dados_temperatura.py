import pandas as pd
import numpy as np
import csv

# Dados de exemplo
data = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
precipitacao = np.random.uniform(0, 10, size=len(data))
max_temp = np.random.uniform(20, 30, size=len(data))
min_temp = np.random.uniform(10, 20, size=len(data))
umidade_ar = np.random.uniform(50, 80, size=len(data))
velocidade_vento = np.random.uniform(5, 15, size=len(data))
media_temp = (max_temp + min_temp) / 2

# Lendo um arquivo
arquivo = open('C:\\Users\\administrador\\Downloads\\Arquivo_dados.csv', 'r')
with open('C:\\Users\\administrador\\Downloads\\Arquivo_dados.csv', 'r') as arquivo:
    dados_temperatura = pd.read_csv(arquivo)
    




# DataFrame
df = pd.DataFrame({
    'data': data,
    'precipitacao': precipitacao,
    'max_temp': max_temp,
    'min_temp': min_temp,
    'umidade_ar': umidade_ar,
    'velocidade_vento': velocidade_vento,
    'media_temp': media_temp
})

df.head()

# Visualização do intervalo de dados em modo texto
def visualizar_intervalo(dados):
    mes_inicial = int(input('Digite o mes inicial: '))
    mes_final = int(input('Digite o mes final: '))
    ano_inicial = int(input('Digite o ano inicial: '))
    ano_final = int(input('Digite o ano final: '))
    
    print("\n Escolha o tipo de dados:")
    print("1 - Todos os dados")
    print("2 - Apenas precipitação")
    print("3 - Apenas temperatura")
    print("4 - Apenas umidade e vento")

    escolha = int(input("Escolha uma opção: "))

    dados_filtrados = []
    
    for i in range(len(dados)):
        dados['data'] = pd.to_numeric(dados['data']).astype(int)
        mes, ano = map(int, str(dados['data'][i]).split('-'))
    
    visualizar_intervalo(dados)

    if mes_inicial <= mes <= mes_final and ano_inicial <= ano <= ano_final:
        if escolha == 1:
            dados_filtrados = dados
        elif escolha == 2:
            dados_filtrados = dados[dados['precipitacao'] > 0]
        elif escolha == 3:
            dados_filtrados = dados[dados['max_temp'] > 0]
        elif escolha == 4:
            dados_filtrados = dados[dados['umidade_ar'] > 0]
            
    # Exibir os dados filtrados
    print("\nDados no período selecionado:")
    for linha in dados_filtrados:
        print(linha)


visualizar_intervalo(df)