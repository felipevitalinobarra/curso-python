"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    o nome de um jogador e quantos gols ele marcou.

    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(jogador='<desconhecido>', gols=0):
    mensagem = (f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
    print('-' * (len(mensagem) + 5))
    print(f'  -> {mensagem}')


def coleta_nome():
    nome = input('Nome do jogador: ').strip().title()
    return nome if nome else '<desconhecido>'


def coleta_gols():
    try:
        return int(input('Número de gols: '))
    except ValueError:
        return 0

def main():
    nome = coleta_nome()
    gols = coleta_gols()
    ficha(nome, gols)


if __name__ == '__main__':
    main()
