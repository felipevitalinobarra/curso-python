"""
Enunciado do Exercício:
    Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela com a formatação correta.
    [  1  ][  2  ][  3  ]
    [  4  ][  5  ][  6  ]
    [  7  ][  8  ][  9  ]
"""

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                num = int(input(f'Digite um valor para [{linha},{coluna}]: '))
                break
            except ValueError:
                print('Valor inválido! Por favor, digite um número inteiro.')
        matriz[linha].append(num)

print('-=-' * 15)
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()
