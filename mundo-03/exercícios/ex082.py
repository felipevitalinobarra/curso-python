"""
Enunciado do Exercício:
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.
"""

def deseja_continuar():
    while True:
        opção = input('Você deseja continuar? [S/N] ').strip().upper()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

números = []
pares = []
ímpares = []

while True:
    try:
        número = int(input('Digite um valor: '))
        números.append(número)

        if número % 2 == 0:
            pares.append(número)
        else:
            ímpares.append(número)

        if deseja_continuar() == 'N':
            break

    except ValueError:
        print('Valor inválido! Por favor, digite um número inteiro.')

print('-=-' * 20)
print(f'A lista completa é: {", ".join(map(str, números))}.')
print(f'Lista de valores pares: {", ".join(map(str, pares)) or "Nenhum número par foi digitado"}.')
print(f'Lista de valores ímpares: {", ".join(map(str, ímpares)) or "Nenhum número ímpar foi digitado"}.')
