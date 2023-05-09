cpf_usuario = '74682489070'
nove_digitos = cpf_usuario[:9]
cont_regressivo_1 = 10
resultado_dig1 = 0

for digito in nove_digitos:
    resultado_dig1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1
digito_1 = (resultado_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_usuario[:9] + str(digito)
cont_regressivo_2 = 11
resultado_dig2 = 0

for digito in dez_digitos:
    resultado_dig2 = int(digito)*cont_regressivo_2
    cont_regressivo_2 -= 1
digito_2 = (resultado_dig2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == cpf_calculo:
    print(f'{cpf_usuario} é válido')
else:
    print('CPF inválido')