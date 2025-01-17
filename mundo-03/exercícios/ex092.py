"""
Enunciado do Exercício:
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO,
    o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposetar (aposentadoria > 35).
"""

from datetime import date

ano_atual = date.today().year
trabalhador = {}

trabalhador['nome'] = input('Nome: ')

while True:
    try:
        nasc = int(input('Ano de Nascimento: '))
        break
    except ValueError:
        print('Entrada inválida! Por favor, digite um ano válido.')

trabalhador['idade'] = ano_atual - nasc        

while True:
    try:
        trabalhador['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))
        break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro.')

if trabalhador['ctps'] != 0:
    while True:
        try:
            trabalhador['contratação'] = int(input('Ano de contratação: '))
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite um ano válido.')

    while True:
        try:
            trabalhador['salário'] = float(input('Salário: R$'))
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite um valor numérico.')

    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35
    trabalhador['anos_para_aposentar'] = trabalhador['aposentadoria'] - ano_atual

print('-=-' * 15)
for chave, valor in trabalhador.items():
    print(f'{chave.capitalize():<20}: {valor}')
