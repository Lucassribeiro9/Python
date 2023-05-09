cpf = '74682489070'
nove_digitos = cpf[:9]
cont_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * cont_regressivo
    cont_regressivo -= 1
digito = (resultado * 10) % 11
digito = digito if digito <= 9 else 0
print(digito)

dez_digitos = cpf[:9] + str(digito)
    