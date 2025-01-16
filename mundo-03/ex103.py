"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    o nome de um jogador e quantos gols ele marcou.

    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

ficha(nome, gols)
