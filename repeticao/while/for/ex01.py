import os

palavra_secreta = 'layout'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print("Você digitou mais de uma letra!")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print("Você acertou!")
        print('A palavra era:', palavra_formada)
        print('Tentativas:', tentativas)
        letras_acertadas = ''
        tentativas = 0