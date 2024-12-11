"""
Enunciado do Exercício:
    Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random

def jogar_jokenpo():
    jokenpo = ['pedra', 'papel', 'tesoura']
    computador = random.choice(jokenpo)

    while True:
        jogador = input('Escolha [pedra, papel ou tesoura]: ').strip().lower()
        if jogador in jokenpo:
            break
        else:
            print('Escolha inválida! Por favor, escolha entre: pedra, papel ou tesoura.')

    print(f"\nComputador escolheu: {computador}")
    print(f"Você escolheu: {jogador}")

    if jogador == computador:
        print("Empatou! Vamos jogar novamente!\n")
        return jogar_jokenpo()  # Reinicia o jogo em caso de empate
    else:
        resultados = {
            ('pedra', 'tesoura'): 'Você ganhou! (pedra quebra tesoura)',
            ('tesoura', 'papel'): 'Você ganhou! (tesoura corta papel)',
            ('papel', 'pedra'): 'Você ganhou! (papel cobre pedra)',
            ('tesoura', 'pedra'): 'Computador ganhou! (pedra quebra tesoura)',
            ('papel', 'tesoura'): 'Computador ganhou! (tesoura corta papel)',
            ('pedra', 'papel'): 'Computador ganhou! (papel cobre pedra)'
        }

        resultado = resultados.get((jogador, computador))
        print(resultado)

# Iniciar o jogo
jogar_jokenpo()
