print(f"{' EXERCÍCIO 23 ':=^30}\n")
"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados.
Ex.: 
Digite um número: 1834
    unidade: 4
    dezena:  3
    centena: 8
    milhar:  1
"""

# Validação de entrada
while True:
    num = input('Digite um número [0-9999]: ')
    if num.isdigit() and 0 <= int(num) <= 9999:
        break
    print('Entrada inválida! Digite apenas números de 0 a 9999.')

# Garantindo 4 dígitos com zfill
num = num.zfill(4)

# Separação dos dígitos
unidade = num[3]
dezena  = num[2]
centena = num[1]
milhar  = num[0]

print(
    f'\nAnalisando o {num}...'
    f'\nMilhar:  {milhar}'
    f'\nCentena: {centena}'
    f'\nDezena:  {dezena}'
    f'\nUnidade: {unidade}'
)
