"""
Enunciado do Exercício:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
    o salário do comprador e em quantos anos ele vai pagar.

    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

formatação = {
    'enunciado': '\033[44m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 36 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        valor_da_casa = float(input('Qual o valor da casa: R$'))
        if valor_da_casa < 50000:
            print(f'\n{formatação["vermelho"]}O valor da casa deve ser maior ou igual a R$50.000,00.{formatação["reset"]}\n')
            continue
        
        salário_do_comprador = float(input('Qual o salário do comprador ? R$'))
        if salário_do_comprador < 1412.00:
            print(f'\n{formatação["vermelho"]}O salário do comprador deve ser maior ou igual ao salário mínimo atual de R$1.412,00\n{formatação["reset"]}')
            continue
        
        anos_pagamento = int(input('Quantos anos para pagar ? '))
        if anos_pagamento <= 0:
            print(f'\n{formatação["vermelho"]}O número de anos deve ser maior que zero.{formatação["reset"]}\n')
            continue
        break
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Por favor digite valores númericos válidos.{formatação["reset"]}')

parcelamento = anos_pagamento * 12
prestação_mensal = valor_da_casa / parcelamento
salário30 = salário_do_comprador * 0.30

if prestação_mensal > salário30:
    print(
            f'\n{formatação["vermelho"]}Empréstimo negado!{formatação["reset"]}'
            f'\nA prestação mensal de R${prestação_mensal:.2f} excede 30% do seu salário ({formatação["vermelho"]}R${salário30:.2f}{formatação["reset"]}).'
         )        
else:
    print(
        f'\n{formatação["verde"]}Empréstimo aprovado!{formatação["reset"]}'
        f'\nSua prestação mensal será de {formatação["verde"]}R${prestação_mensal:.2f}{formatação["reset"]}.'
        )