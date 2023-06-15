while True:
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = a / b
        print(c)
        break
    except ValueError:
        print("Erro: valor inválido. Digite um número inteiro.")
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    except Exception as e:
        print("Erro desconhecido:", e)
