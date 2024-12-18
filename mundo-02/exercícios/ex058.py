"""
Enunciado do Exercício:
    Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

tentativas = 0
computador = randint(0,10)

print('=*=' * 21)
print('O computador pensou em um número entre 0 e 10. Tente adivinhar!')
print('=*=' * 21)

while True:
    tentativas += 1
    jogador = int(input('\nQual é seu palpite: '))
    
    if jogador == computador:
        if tentativas == 1:
            print('\n🎉PARABÉNS! Você adivinhou na primeira tentativa.')
        else:
            print(f'\n🎉PARABÉNS! Você adivinhou na {tentativas}ª tentativa.')
        print(f'O número pensado foi [{computador}].')
        break
    elif jogador < computador:
        print('\n🔼 Tente um número maior!')
    else:
        print('\n🔽 Tente um número menor!')
