"""
Enunciado do Exercício:
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o Corinthians.
"""
print(f'{" BRASILEIRÃO 2017 ":=^50}')

tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo',
          'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'\nA) Os cinco primeiros colocados são: {", ".join(tabela[:5])}')
print(f'\nB) Os quatro últimos são: {", ".join(tabela[-4:])}')
print(f'\nC) Tabela em ordem alfabética [A/Z]: {", ".join(sorted(tabela))}')
time_procurado = input('\nDeseja ver a colocação de qual time? ').strip()
if time_procurado in tabela:
    print(f'\nD) O {time_procurado} ficou na {tabela.index(time_procurado) + 1}ª colocação.')
else:
    print(f'\nD) O {time_procurado} não está na tabela do Brasileirão de 2017.')
