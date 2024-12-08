"""
Enunciado do Exercício: 
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

    O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'branco': '\033[7;30;44m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 28 ":=^30}{formatação["reset"]}\n')

# O computador escolhe um número
computador = randint(0, 5)

# Introdução ao jogo
print(f'{formatação["azul"]}-=-' * 20)
print(f'{formatação["branco"]}Vou pensar em um número entre 0 e 5. Tente adivinhar...{formatação["reset"]}')
print(f'{formatação["azul"]}-=-' * 20, f'{formatação["reset"]}\n')

# Validação da entrada do usuário
while True:
    try:
        jogador = int(input('Em que número eu pensei ? '))
        if 0 <= jogador <= 5:
            break
        else:
            print(f'{formatação["vermelho"]}Por favor, escolha um número entre 0 e 5.{formatação["reset"]}')
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Digite apenas números inteiros.{formatação["reset"]}')

# Processamento e resultado
print('\nPROCESSANDO...')
sleep(1)

if jogador == computador:
    print(f'\n{formatação["verde"]}PARABÉNS!{formatação["reset"]} Você conseguiu me vencer! Eu realmente pensei no número {computador}.')
else:
    print(f'\n{formatação["vermelho"]}GANHEI!{formatação["reset"]} Eu pensei no número {computador} e não no {jogador}.')
