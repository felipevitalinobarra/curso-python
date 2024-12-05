print(f"{' EXERCÍCIO 28 ':=^30}\n")
"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

computador = randint(0,5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei ? '))

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('\nPARABÉNS! Você conseguiu me vencer =D')
else:
    print(f'\nGANHEI! Eu pensei no número {computador} e não no {jogador}.')
