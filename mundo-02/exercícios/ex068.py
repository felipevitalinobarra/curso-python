"""
Enunciado do Exercício:
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('=-='*12)
print(' 🎮  VAMOS JOGAR PAR OU ÍMPAR   🎲')
print('=-='*12)

vitórias = 0

while True:
    computador = randint(0,10)
    try:
        jogador = int(input('Diga um valor: '))
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro.\n')
        continue

    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    if escolha not in 'PI':
        print('Escolha inválida! Digite "P" para Par ou "I" para Ímpar.\n')
        continue
    
    print('~'*36)

    total = computador + jogador
    par = total % 2 == 0

    print(f'\nVocê jogou {jogador} e o computador {computador}. Total de {total}, deu {"PAR" if par else "ÍMPAR"}.')

    if (escolha == 'P' and par) or (escolha == 'I' and not par):
        print('\nVocê VENCEU! 🏆')
        print('-'*36)
        vitórias += 1
    else:
        print('\nVocê PERDEU! 😔')
        print(f'GAME OVER! Você venceu {vitórias} {"vez" if vitórias == 1 else "vezes"}.')
        break
