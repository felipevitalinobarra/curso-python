"""
Enunciado do Exercício:
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""

def deseja_continuar():
    while True:
        opção = input('Você deseja continuar? [S/N] ').strip().upper()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

pessoas = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])

    if deseja_continuar() == 'N':
        break

# Determinação de maior e menor peso.
pesado = max(pessoas, key=lambda x: x[1])[1]
leve = min(pessoas, key=lambda x: x[1])[1]

# Listas para armazenar os mais pesados e mais leves.
pesados = [pessoa[0] for pessoa in pessoas if pessoa[1] == pesado]
leves = [pessoa[0] for pessoa in pessoas if pessoa[1] == leve]

print('-=-' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {pesado:.2f}Kg. Peso de {", ".join(pesados)}.')
print(f'O menor peso foi {leve:.2f}Kg. Peso de {", ".join(leves)}.')
