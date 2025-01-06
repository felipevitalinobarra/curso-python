"""
Enunciado do Exercício:
    Aprimore o anterior, mostrando no final:

    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
pares = ter_coluna = 0

for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                num = int(input(f'Digite um valor para [{linha},{coluna}]: '))
                break
            except ValueError:
                print('Valor inválido! Por favor, digite um número inteiro.')
        matriz[linha].append(num)        

# Exibe a matriz formatada
print('-=-' * 15)
for linha in matriz:
    for elemento in linha:
        print(f'[{elemento:^5}]', end='')
    print()

# Cálculos
for linha in matriz:
    # Soma da terceira coluna (índice 2)
    ter_coluna += linha[2]
    # Soma dos valores pares
    for elemento in linha:
        if elemento % 2 == 0:
            pares += elemento

# Maior valor da segunda linha (índice 1)
maior = max(matriz[1])

print('-=-' * 15)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {ter_coluna}.')
print(f'Maior valor da segunda linha {maior}.')
