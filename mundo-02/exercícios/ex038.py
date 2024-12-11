"""
Enunciado do Exercício:
    Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    > O primeiro valor é maior
    > O segundo valor é maior
    > Não existe valor maior, os dois são iguais
"""

from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 38 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        n1 = int(input(f'Digite um número inteiro: {formatação["verde"]}'))
        n2 = int(input(f'{formatação["reset"]}Digite outro número inteiro: {formatação["verde"]}'))

        print(f'\n{formatação["reset"]}{formatação["azul"]}Analisando Resultado...{formatação["reset"]}')
        sleep(1)

        if n1 > n2:
            print(f'\n{formatação["verde"]}O primeiro valor ({n1}) é maior que o segundo ({n2}).{formatação["reset"]}')
        elif n2 > n1:
            print(f'\n{formatação["verde"]}O segundo valor ({n2}) é maior que o primeiro ({n1}).{formatação["reset"]}')
        else:
            print(f'\n{formatação["vermelho"]}Não existe valor maior, os dois são iguais.{formatação["reset"]}')
        break

    except ValueError:
        print(f'{formatação["vermelho"]}Valor inválido! Por favor, informe um número inteiro.{formatação["reset"]}')
