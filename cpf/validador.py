import re
import sys

cpf_entrada = input('Digite seu cpf: ')
cpf_digitado = re.sub(r'[^0-9]', '', cpf_entrada)

cpf_sequencial = cpf_entrada == cpf_entrada[0] * len(cpf_entrada)

if cpf_sequencial:
    print('Você enviou dados sequenciais!!')
    sys.exit()

nove_digitos = cpf_digitado[:9]
cont_regressivo_1 = 10
result_dig1 = 0
for digito in nove_digitos:
    result_dig1 += int(digito) * cont_regressivo_1
    cont_regressivo_1 -= 1
digito_1 = (result_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
cont_regressivo_2 = 11
result_dig2 = 0

for digito in dez_digitos:
    result_dig2 += int(digito) * cont_regressivo_2
    cont_regressivo_2 -= 1
digito_2 = (result_dig2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_entrada == cpf_gerado_pelo_calculo:
    print(f'{cpf_entrada} é válido')
else:
    print('CPF inválido')