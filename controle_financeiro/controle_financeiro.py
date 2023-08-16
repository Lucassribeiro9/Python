class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.recebimentos = []
        self.gastos = []

    def adicionar_recebimento(self, valor):
        self.recebimentos.append(valor)

    def adicionar_gasto(self, valor):
        self.gastos.append(valor)

    def calcular_total_recebimentos(self):
        return sum(self.recebimentos)

    def calcular_total_gastos(self):
        return sum(self.gastos)


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.recebimentos = []
        self.gastos = []

    def adicionar_recebimento(self, valor):
        self.recebimentos.append(valor)

    def adicionar_gasto(self, valor):
        self.gastos.append(valor)

    def calcular_total_recebimentos(self):
        return sum(self.recebimentos)

    def calcular_total_gastos(self):
        return sum(self.gastos)


class Transacao:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class FluxoDeCaixa:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def calcular_saldo(self):
        saldo = 0
        for transacao in self.transacoes:
            saldo += transacao.valor
        return saldo


# Criar empresas
empresas = []
empresas.append(Empresa("Empresa A"))
empresas.append(Empresa("Empresa B"))
empresas.append(Empresa("Empresa C"))
empresas.append(Empresa("Empresa D"))
empresas.append(Empresa("Empresa E"))

# Criar bancos
bancos = []
bancos.append(Banco("Banco A"))
bancos.append(Banco("Banco B"))
bancos.append(Banco("Banco C"))
bancos.append(Banco("Banco D"))
bancos.append(Banco("Banco E"))

fluxo_de_caixa = FluxoDeCaixa()

while True:
    print("1. Adicionar receita da empresa")
    print("2. Adicionar despesa da empresa")
    print("3. Adicionar receita do banco")
    print("4. Adicionar despesa do banco")
    print("5. Calcular saldo do fluxo de caixa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_empresa = input("Nome da empresa: ")
        empresa = next((e for e in empresas if e.nome == nome_empresa), None)
        if empresa:
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor da receita: "))
            empresa.adicionar_recebimento(valor)
            fluxo_de_caixa.adicionar_transacao(Transacao(descricao, valor))
            print("Receita adicionada com sucesso!")
        else:
            print("Empresa não encontrada.")

    elif opcao == "2":
        nome_empresa = input("Nome da empresa: ")
        empresa = next((e for e in empresas if e.nome == nome_empresa), None)
        if empresa:
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor da despesa: "))
            empresa.adicionar_gasto(valor)
            fluxo_de_caixa.adicionar_transacao(Transacao(descricao, -valor))
            print("Despesa adicionada com sucesso!")
        else:
            print("Empresa não encontrada.")

    elif opcao == "3":
