"""
Enunciado do Exercício:
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
    sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for chave, valor in jogadores.items():
    print(f'O {chave} tirou {valor} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

"""
Outra solução: Usar o itemgetter
    from operator import itemgetter
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
"""

print('-' * 30)
print('Ranking dos jogadores:')
for i, (jogador, valor) in enumerate(ranking, 1):
    print(f'{i}º lugar: {jogador} com {valor}.')
    sleep(1)
