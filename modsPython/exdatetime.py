# Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos. 
# A data em que ela pegou o empréstimo foi 20/12/2017 e o vencimento de cada parcela 
# Crie a data de vencimento
# Crie a data final do empréstimo
# Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = float(input('Digite o valor do empréstimo: '))
data_emprestimo = datetime(2024, 1, 20)
qtd_parcelas = int(input('Digite em quantas parcelas deseja pagar: '))
data_parcelas = []
data_parcela = data_emprestimo

for _ in range(qtd_parcelas):
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)
valor_parcela = valor_emprestimo / qtd_parcelas
for i, data in enumerate(data_parcelas):
    print(f'Parcela {i+1} - Data: {data.strftime('%d/%m/%Y')} - Valor da parcela: R${valor_parcela:.2f}')
print()

print(f'Total de parcelas: {qtd_parcelas}')
print(f'Valor de cada parcela: {valor_parcela:.2f}')

    



