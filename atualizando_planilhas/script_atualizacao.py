from cpplanilhas import executar_atualizacao

def atualizar_planilha():
    try:
        executar_atualizacao()
        print("Processo concluido com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar planilha: {e}")

atualizar_planilha()