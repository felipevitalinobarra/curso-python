"""
Enunciado do Exercício:
    Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

from time import sleep

def deseja_continuar():
    while True:
        opção = input('\nDeseja continuar? [S/N] ').strip().upper()
        print()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

def buscar_jogador(jogadores):
    while True:
        print('-' * 50)
        try:
            j = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
            if j == 999:
                print('Encerrando visualização de jogadores...')
                break
            elif 0 <= j < len(jogadores):
                jogador = jogadores[j]
                print(f'\nEstatísticas do {jogador["nome"]}:')
                for i, g in enumerate(jogador["gols"]):
                    print(f'{"=>":>5} Na partida {i+1} fez {g} {"gol" if g == 1 else "gols"}.')
            else:
                print('-' * 48)
                print('Jogador não encontrado! Digite um número de indíce válido.')
        except ValueError:
            print('-' * 48)
            print('Entrada inválida! Por favor, digite um número inteiro.')

def main():
    jogadores = []
    while True:
        jogador = {}
        gols = []
        print('-' * 30)
        jogador['nome'] = input('Nome do jogador: ').strip().title()

        while True:
            try:
                p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
                if p < 0:
                    print('Digite um número positivo')
                else:
                    break
            except ValueError:
                print('Entrada inválida! Por favor, digite um número inteiro.')

        for i in range(p):
            while True:
                try:
                    gol = int(input(f'Quantos gols na {i+1}º partida? '))
                    if gol < 0:
                        print('Digite um número positivo.')
                    else:
                        gols.append(gol)
                        break
                except ValueError:
                    print('Entrada inválida! Por favor, digite um número inteiro')
        
        jogador['gols'] = gols
        jogador['total'] = sum(gols)
        jogadores.append(jogador.copy())
        
        if deseja_continuar() == 'N':
            break

    print(f'{"COD":<5} {"NOME":<15} {"GOLS":<20} {"TOTAL":<5}')
    for i, jogador in enumerate(jogadores):
        print(f'{i:<5} {jogador["nome"]:<15} {str(jogador["gols"]):<20} {jogador["total"]:<5}')

    buscar_jogador(jogadores)
    sleep(1)
    print('FINALIZANDO...\nVOLTE SEMPRE! 👋🏽')
main()
