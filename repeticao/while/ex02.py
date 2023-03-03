frase = "If Young Metro Don't Trust You, I'm Gon'Shoot You"

i = 0
qtd_apmais_vezes = 0
letra_aparecer_mvezes = ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == '':
        i += 1
        continue

    qtd_apmais_vezes_atual = frase.count(letra_atual)

    if qtd_apmais_vezes <= qtd_apmais_vezes_atual:
        qtd_apmais_vezes = qtd_apmais_vezes_atual
        letra_aparecer_mvezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi {letra_aparecer_mvezes}'
          f' e a quantidade foi {qtd_apmais_vezes}x')
