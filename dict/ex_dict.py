perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

participantes = {}
qtd_participantes = 0
qtd_acertos = 0

while True:
    try:
        qtd_participantes = int(input("Digite a quantidade de participantes: "))
        if qtd_participantes <= 0:
            print("A quantidade de participantes deve ser maior que zero.")
            continue
        break
    except ValueError:
        print("Valor inválido")

    for i in range(qtd_participantes):
        while True:
            participante = input("Digite o nome do participante: ")
            if participante.isalpha():
                break
            else:
                print("Nome inválido.")

for pergunta in perguntas:
    print("Pergunta: ", pergunta["Pergunta"])
    print()

    opcoes = pergunta["Opções"]
    for i, opcao in enumerate(opcoes):
        print(f"{i})", opcao)
    print()
    for participante in participantes:
        escolha = input(f'{participante} escolha uma opção: ')
        escolha_int = None
        acertou = False
        qtd_opcoes = len(opcoes)

        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta["Resposta"]:
                    acertou = True
        participantes[participante].append(acertou)
        if acertou:
            qtd_acertos += 1
            print("Acertou 👍")
        else:
            print("Errou")

    print()

print("Resultados:")
for participante, respostas in participantes.items():
    qtd_acertos = sum(respostas)
    print(f"{participante}: {qtd_acertos} acertos de {len(perguntas)}")