"""
Enunciado do Exercício:
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

    > À vista dinheiro/cheque: 10% de desconto
    > À vista no cartão: 5% de desconto
    > Em até 2x no cartão: preço normal
    > 3x ou mais no cartão: 20% de juros
"""

while True:
    try:
        valor_produto = float(input('Qual o preço do produto? R$'))
        break
    except ValueError:
        print('Valor inválido! Por favor, insira um número válido.\n')

print(
    '\nEscolha a forma de pagamento:\n'
    '[ 1 ] À vista no dinheiro ou cheque (10% de desconto)\n'
    '[ 2 ] À vista no cartão (5% de desconto)\n'
    '[ 3 ] Em até 2x no cartão (sem juros)\n'
    '[ 4 ] 3x ou mais no cartão (20% de juros)'
)

while True:
    try:
        forma_de_pagamento = int(input('\nQual é a opção: '))

        if forma_de_pagamento == 1:
            total = valor_produto * 0.90
            print(f'\nPagando à vista no dinheiro ou cheque, o total com 10% de desconto será R${total:.2f}.')
        elif forma_de_pagamento == 2:
            total = valor_produto * 0.95
            print(f'\nPagando à vista no cartão, o total com 5% de desconto será R${total:.2f}.')
        elif forma_de_pagamento == 3:
            parcela = valor_produto / 2
            print(f'\nPagando em até 2x no cartão, o valor será 2 parcelas de R${parcela:.2f}, totalizando R${valor_produto:.2f}.')
        elif forma_de_pagamento == 4:
            parcelas = int(input('Quantas parcelas? '))
            total = valor_produto * 1.20
            parcela = total / parcelas
            print(f'\nParcelando em {parcelas}x, o valor total com 20% de juros será R${total:.2f}, com parcelas de R${parcela:.2f}.')
        else:
            print('Opção inválida! Por favor, escolha uma opção entre 1 e 4.\n')
            continue
        break
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.\n')
