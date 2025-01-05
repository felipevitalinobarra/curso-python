"""
Enunciado do Exercício:
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
    para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

print('-' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-' * 30)

while True:
    try:
        qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
        if qtd_jogos > 0:
            break
        print('Por favor, insira um número positivo.')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.')

jogos = []
jogo = []

for _ in range (0, qtd_jogos):
    for i in range(0,6):
        while True:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                break
    jogos.append(jogo[:])
    jogo.clear()        

print(f'{" SORTEANDO " + str(qtd_jogos) + " JOGOS ":=^30}')

for i, jogo in enumerate(jogos, start=1):
    sleep(1)
    print(f'Jogo {i}: {", ".join(map(str,sorted(jogo))):^10}')
print(f'{" < BOA SORTE ! > ":=^30}')
