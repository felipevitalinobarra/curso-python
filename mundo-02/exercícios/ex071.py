"""
Enunciado do Exercício:
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
    e o programa vai informar quantas cédulas de cada valor serão entregues.

    Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('=' * 40)
print(f'{" B A N C O  E L  B A R R A ":=^40}')
print('=' * 40)

try:
    saque = int(input('Que valor você quer sacar? R$'))

    if saque < 1:
        print('\nValor inválido. O saque deve ser maior que zero.')

    else:
        print()
        cédulas = 0

        if saque >= 50:
            cédulas = saque // 50
            saque = saque - (cédulas * 50)
            print(f'Total de {cédulas} {"cédula" if cédulas == 1 else "cédulas"} de R$50')
        if saque >= 20:
            cédulas = saque // 20
            saque = saque - cédulas * 20
            print(f'Total de {cédulas} {"cédula" if cédulas == 1 else "cédulas"} de R$20')
        if saque >= 10:
            cédulas = saque // 10
            saque = saque - cédulas * 10
            print(f'Total de {cédulas} {"cédula" if cédulas == 1 else "cédulas"} de R$10')
        if saque >= 1:
            cédulas = saque // 1
            saque = saque - cédulas * 1
            print(f'Total de {cédulas} {"cédula" if cédulas == 1 else "cédulas"} de R$1')  

    print('='*40)
    print('Volte sempre ao BANCO EL BARRA! Tenha um excelente dia!')
except ValueError:
    print('='*40)
    print('Entrada inválida! Por favor, digite um valor inteiro.')
