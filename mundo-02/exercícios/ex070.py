"""
Enunciado do Exercício:
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$1000,00.
    C) Qual é o nome do produto mais barato.
"""

total = mais_de_mil = 0
mais_barato = float('inf')
produto_mais_barato = ''

print('=*=' * 17)
print(f'{"S U P E R   S T O R E":^52}')
print('=*=' * 17)

while True:
    nome = input('\nNome do produto: ').strip()
    
    try:
        preço = float(input('R$'))
    except ValueError:
        print('Valor inválido! Por favor, digite um valor correto, tente novamente!')
        continue

    total += preço

    if preço > 1000:
        mais_de_mil += 1

    if preço < mais_barato:
        mais_barato = preço
        produto_mais_barato = nome

    print('-' * 50)
    opção = input('Deseja continuar? [S/N] ').strip().upper()

    if opção not in 'SN':
        print('\nOpção inválida! Por favor, digite "S" para prosseguir ou "N" para encerrar.')
        continue
    if opção == 'N':
        break

print('='*50)
print(f'{" R E L A T Ó R I O ":=^50}')
print('='*50)

print(f'\nA) Total da compra R${total:.2f}')
print(f'B) {mais_de_mil} {"produto custa" if mais_de_mil == 1 else "produtos custam"} mais de R$1000.00')
print(f'C) O produto mais barato foi {produto_mais_barato} que custou {mais_barato:.2f}')
