"""
Enunciado do Exercício
    Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = {}
gols = []

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

print('-=-' * 10)
for chave, valor in jogador.items():
    print(f'{chave.capitalize():<10}: {valor}')
print('-=-' * 10)

for i, g in enumerate(gols):
    print(f'{"=>":>5} Na partida {i+1}, fez {g} {"gol" if g == 1 else "gols"}.')

print('-=-' * 10)
print(f'O jogador {jogador["nome"]} jogou {p} partidas e fez um total de {jogador["total"]} {"gol" if jogador["total"] == 1 else "gols"}.')
