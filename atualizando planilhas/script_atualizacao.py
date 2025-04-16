import schedule
import time
from cpplanilhas import executar_atualizacao

def atualizar_planilha():
    executar_atualizacao()

schedule.every(7).days.at("08:00").do(atualizar_planilha)  # execute a cada 7 dias, às 08:00

while True:
    schedule.run_pending()
    time.sleep(1)