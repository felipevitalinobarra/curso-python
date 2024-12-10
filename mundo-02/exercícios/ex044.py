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

while True:
    try:
        forma_de_pagamento = int(input(
            '\nQual a forma de pagamento:\n'
            'Digite 1 para: À vista no dinheiro ou cheque.\n'
            'Digite 2 para: À vista no cartão.\n'
            'Digite 3 para: Em até 2x no cartão.\n'
            'Digite 4 para: Em até 3x ou mais no cartão.\n\nEscolha: '
        ))
        
        if forma_de_pagamento == 1:
            desconto = valor_produto - (valor_produto * 0.10)
            print(f'\nPagando à vista no dinheiro ou cheque, o produto que custava R${valor_produto:.2f}, '
                  f'custará R${desconto:.2f} com 10% de desconto.')
            break
        elif forma_de_pagamento == 2:
            desconto = valor_produto - (valor_produto * 0.05)
            print(f'\nPagando à vista no cartão, o produto que custava R${valor_produto:.2f}, '
                  f'custará R${desconto:.2f} com 5% de desconto.')
            break
        elif forma_de_pagamento == 3:
            print(f'\nPagando em até 2x no cartão, o produto custará o preço normal que é R${valor_produto:.2f}.')
            break
        elif forma_de_pagamento == 4:
            juros = valor_produto + (valor_produto * 0.20)
            print(f'\nPagando em até 3x ou mais no cartão, o produto que custava R${valor_produto:.2f}, '
                  f'custará R${juros:.2f}.')
            break
        else:
            print('Escolha inválida! Por favor, digite um número de 1 a 4.\n')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro de 1 a 4.\n')
