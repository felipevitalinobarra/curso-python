"""
Enunciado do Exercício:
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        número = int(input('Digite um número entre 0 e 20: '))
        if 0 <= número <= 20:
            print(f'\nVocê digitou o número {cont[número]}.')
        else:
            print('\nNúmero fora do intervalo! Tente novamente.\n')
            continue
    except ValueError:
        print('\nEntrada inválida! Por favor, digite um número inteiro.\n')
        continue

    while True:
        opção = input('\nVocê quer continuar? [S/N] ').strip().upper()

        if opção in ('S','N'):
            break
        print('\nOpção inválida! Por favor, digite "S" para sim ou "N" para não.')
        
    if opção == 'N':
        print('\nPrograma encerrado. Até a próxima!')
        break
